import subprocess

import ollama
from django.http import JsonResponse

from django.http import HttpResponse
from transformers import AutoModelForCausalLM, AutoTokenizer
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
        #logger.info('You typed: %s', text)
        if len(text)>3:
        # Call the run_llama_model function with the user's text
            llama_response = run_llama_model(user_prompt=text)


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



def run_llama_model(user_prompt):
    try:
        prompt = (
            "Generate a response in the following format:\n\n"
            "1. Introduction\n"
            "2. References\n"
            "3. Detailed Response\n"
            "4. Related Questions with Answers\n"
            "5. Include images and graphics where required\n\n"
            "Question: " + str(user_prompt) + "\n\n"
        )

        response = ollama.generate(model='llama3', prompt=prompt)

        # Check if 'response' key exists and return it
        if 'response' in response:
            return response['response']

        # If 'response' key does not exist, return the entire response
        return response

    except Exception as e:
        logger.error('Exception occurred: %s', str(e))
        return {'error': str(e)}

