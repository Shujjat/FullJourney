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
    return get_dummy_response()
    # try:

    #
    #
    #     prompt = (
    #         "Generate a response in the following format:\n\n"
    #         "1. Introduction\n"
    #         "2. References\n"
    #         "3. Detailed Response\n"
    #         "4. Related Questions with Answers\n"
    #         "5. Include images and graphics where required\n\n"
    #         "Question: " + str(user_prompt) + "\n\n"
    #     )
    #
    #     response = ollama.generate(model='llama3', prompt=prompt)
    #
    #     # Check if 'response' key exists and return it
    #     if 'response' in response:
    #         return response['response']
    #
    #     # If 'response' key does not exist, return the entire response
    #     return response
    #
    # except Exception as e:
    #     logger.error('Exception occurred: %s', str(e))
    #     return {'error': str(e)}

def get_dummy_response():
    return {
        'response': """
                        
                **1. Dummy Introduction**
                
                Coulomb's law, named after Charles-Augustin de Coulomb, is a fundamental principle in electrostatics that describes the interaction between two charged particles or objects. It is a crucial concept in understanding the behavior of electric charges and their effects on other charges and matter.
                
                **2. References**
                
                * Coulomb, C. A. (1785). Exériences sur le magnétisme et la Electricity.
                * Griffiths, D. J. (1999). Introduction to Electrodynamics. Prentice Hall.
                * Tipler, P. A., & Mosca, G. (2008). Physics for Scientists and Engineers. W.H. Freeman and Company.
                
                **3. Detailed Response**
                
                Coulomb's law states that the force of attraction or repulsion between two charged particles is proportional to the product of their magnitudes (charges) and inversely proportional to the square of the distance between them. Mathematically, this can be expressed as:
                
                F = k \* q1 \* q2 / r^2
                
                where:
                
                * F is the force of attraction or repulsion between the two charges
                * k is Coulomb's constant (approximately 8.99 × 10^9 N m^2 C^-2)
                * q1 and q2 are the magnitudes (charges) of the two particles
                * r is the distance between the centers of the two particles
                
                **Examples:**
                
                Let's consider a few examples to illustrate Coulomb's law:
                
                Example 1: Two identical charges with magnitude +q1 (positive charge) separated by a distance r.
                
                In this case, the force F between the charges will be attractive, and we can calculate it using Coulomb's law:
                
                F = k \* q1^2 / r^2
                
                Example 2: A positive charge +q1 and a negative charge -q2 with magnitude equal to |q1| (opposite sign) separated by a distance r.
                
                In this case, the force F between the charges will be repulsive, and we can calculate it using Coulomb's law:
                
                F = k \* q1 \* (-q2) / r^2
                
                **4. Related Questions with Answers**
                
                Q: What are the units of Coulomb's constant (k)?
                A: The units of Coulomb's constant (k) are Newtons per Coulomb-squared meter (N m^2 C^-2).
                
                Q: Can Coulomb's law be used to predict the force between two charges at any distance?
                A: No, Coulomb's law only applies when the charges are stationary and not moving. For moving charges, we need to use more advanced theories like electromagnetism.
                
                **5. Images and Graphics**
                
                [Insert an image or graphic illustrating Coulomb's law, such as a diagram showing the forces between two charged particles]
                
                I hope this helps! Let me know if you have any further questions or need additional clarification.
                [16/Jun/2024 08:41:26] "POST /lms/index.html HTTP/1.1" 200 2565
                INFO 2024-06-16 08:41:51,528 _client _client.py 1026 HTTP Request: POST http://127.0.0.1:11434/api/generate "HTTP/1.1 200 OK"
                INFO 2024-06-16 08:41:51,529 views views.py 32 Received Response Here is a response in the requested format:
                
                **1. Introduction**
                
                Coulomb's Law, also known as Coulomb's Inverse Square Law, is a fundamental concept in electrostatics that describes the relationship between two charges. It was first formulated by Charles-Augustin de Coulomb in 1785 and has since become a cornerstone of understanding electric forces. In this response, we will explore Coulomb's Law with examples to help illustrate its significance.
                
                **2. References**
                
                * Coulomb, C.-A. (1785). Mémoire sur la formation proportionnelle des deux électricités. Histoire de l'Académie Royale des Sciences, 89-109.
                * Griffiths, D. J. (2013). Introduction to Electrodynamics. Pearson Education.
                
                **3. Detailed Response**
                
                Coulomb's Law states that the force between two point charges is proportional to the product of their magnitudes and inversely proportional to the square of the distance between them. Mathematically, this can be expressed as:
                
                F = k \* (q1 \* q2) / r^2
                
                where F is the electrostatic force between the two charges, k is Coulomb's constant, q1 and q2 are the magnitudes of the two charges, and r is the distance between their centers.
                
                **Example 1: Two Like Charges**
                
                Suppose we have two positively charged particles with equal magnitude, separated by a distance of 10 cm. Using Coulomb's Law, we can calculate the force between them:
                
                F = k \* (q1 \* q2) / r^2
                = k \* (5.0 × 10^-6 C \* 5.0 × 10^-6 C) / (0.10 m)^2
                ≈ 9.8 × 10^-3 N
                
                Since both charges are positive, the force between them is repulsive.
                
                **Example 2: Two Opposite Charges**
                
                Now, suppose we have a positively charged particle and a negatively charged particle with equal magnitude, separated by the same distance of 10 cm. Again, using Coulomb's Law:
                
                F = k \* (q1 \* q2) / r^2
                = k \* (5.0 × 10^-6 C \* -5.0 × 10^-6 C) / (0.10 m)^2
                ≈ 9.8 × 10^-3 N
                
                Since the charges are opposite, the force between them is attractive.
                
                **4. Related Questions with Answers**
                
                Q: What is the value of Coulomb's constant k?
                A: The value of Coulomb's constant k is approximately 8.99 × 10^9 N m^2 C^-2.
                
                Q: How does Coulomb's Law change if one or both charges are moving?
                A: When one or both charges are moving, the force between them becomes dependent on their velocities and directions. This is known as electromagnetic induction and is described by Maxwell's equations.
                
                **5. Include images and graphics where required**
                
                Unfortunately, this response does not require any images or graphics. However, if you would like to see visual representations of Coulomb's Law in action, I can provide some examples:
                
                * An animation showing the force between two charges as they move closer or farther apart
                * A diagram illustrating the electric field lines around a charged particle
                * A graphic comparing the forces between different pairs of charges (e.g., like-like, opposite-opposite, etc.)
        """
    }