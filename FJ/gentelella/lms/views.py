import os
import fitz
import re
from PIL import Image
import pytesseract
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from django import template

register = template.Library()
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import ollama
import logging

logger = logging.getLogger(__name__)


def lmsv(request):
    context = {}
    template = loader.get_template('lms/aindex.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
def index(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        # logger.info('You typed: %s', text)
        if len(text) > 3:
            # Call the run_llama_model function with the user's text
            llama_response = run_llama_model(user_prompt=text, use_dummy_response=False)

            logger.info('Received Response %s', llama_response)
            # logger.error('Llama Model Error: %s', llama_response)
            # logger.error(vars(llama_response))

            if 'error' in llama_response:
                return JsonResponse({'error': llama_response['error']}, status=500)

            return JsonResponse({'response': llama_response}, safe=False)

    context = {}

    load_template = 'lms/classroom.html'
    template = loader.get_template(load_template)
    return HttpResponse(template.render(context, request))


def run_llama_model(user_prompt, use_dummy_response=True):

    try:
        background_hint = "learner is atmost 18 years of age or more. "
        avoid = 'nudity and foul language'
        pdf=read_pdf()

        prompt = (
                "Generate a course with the given title and provide details as follows: \n\n"
                "1. Introduction\n"
                "2. Give list of modules in the course\n"
                "3. Lessons under each module\n"
                "4. Brief Description of each module and lesson\n"
                "5. Use data provided here as base for the course "+pdf+ "\n"

        )
        print(prompt)
        response = ollama.generate(model='llama3', prompt=prompt)

        if isinstance(response, dict):
            print("The response is a dictionary. Here are the keys:")
            for key in response.keys():
                print(key)
        else:
            print(f"The response is of type: {type(response)}")

        with open("response.txt", "w+") as file:
            file.write(str(response['response']))
            logger.error(str(response))
        return response

    except Exception as e:
        logger.error('Exception occurred: %s', str(e))
        return {'error': str(e)}


@csrf_exempt
def read_pdf():
    # Open the PDF file
    book_name='WordPress'
    source_book_extension='.pdf'
    output_book_extension='.txt'
    source_file_path = 'gentelella/lms/books/'+book_name+source_book_extension
    output_file_path = 'gentelella/lms/books/'+book_name+output_book_extension
    doc = fitz.open(source_file_path)

    text_list = []  # List to store extracted text from each page

    try:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)

            # Get the pixmap (image) of the page
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes("png")))

            # Perform OCR on the image
            text = pytesseract.image_to_string(img)

            # Print or process the extracted text
            print(f"Page {page_num + 1}:\n{text}\n")

            text_list.append(text)  # Append text to the list

        # Close the PDF file
        doc.close()

        with open(output_file_path, "w+") as file:
            file.write(str(text_list))
        # Return the extracted text as JSON response
        chapters = extract_chapters_and_items(text_list)
        return text_list

    except Exception as e:
        # Handle exceptions if any occur
        return JsonResponse({'error': str(e)}, status=500)
@csrf_exempt
def extract_topics_from_file( text_file_path=None):

    text_file_path = 'gentelella/lms/books/Inter-I-Physics.txt'
    topics_file_path = 'gentelella/lms/books/topics-Inter-I-Physics.txt'
    if not os.path.isfile(text_file_path):
        raise FileNotFoundError(f"The file {text_file_path} does not exist.")

    with open(text_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Create a prompt to ask the AI to extract topics
    prompt = f"Extract all distinct topics from the following text:\n\n{file_content}"

    try:
        response = generate_response(prompt)

        with open(topics_file_path, "w+") as file:
            file.write(str(response))
        return response
    except Exception as e:
        raise RuntimeError(f"Error generating response: {e}")
@csrf_exempt
def extract_chapters_and_items(text=None, text_file_path=None):

    text_file_path = 'gentelella/lms/books/Inter-I-Physics.txt'
    if text_file_path:
        with open(text_file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Debug: Print type of text
    print(f"Type of text: {type(text)}")

    if not text:
        return {"error": "No text provided for processing."}

    chapters = []
    current_chapter = None

    lines = text.split("\n")
    chapter_pattern = re.compile(r"^Chapter \d+:\s*(.*)$", re.IGNORECASE)  # Pattern for chapter names
    item_pattern = re.compile(r"^\d+\.\s*(.*)$")  # Pattern for items (numbered list)

    for line in lines:
        line = line.strip()

        # Match chapter names
        chapter_match = chapter_pattern.match(line)
        if chapter_match:
            if current_chapter:
                chapters.append(current_chapter)
            current_chapter = {
                "chapter_name": chapter_match.group(1),
                "items": []
            }
            continue

        # Match items
        item_match = item_pattern.match(line)
        if item_match and current_chapter:
            print(current_chapter)
            current_chapter["items"].append(item_match.group(1))

    # Append the last chapter
    if current_chapter:
        chapters.append(current_chapter)

    return chapters
def generate_response(prompt):
    response = ollama.generate(model='llama3', prompt=prompt)
    return response
