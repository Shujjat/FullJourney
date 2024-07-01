from django.urls import path, re_path
from lms import views


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django lms.
    re_path(r'^.*\.htm', views.index, name='lmslms'),
    path('lms', views.lmsv, name='lms'),
    path('lms/llama/', views.run_llama_model, name='llama'),
    path('lms/ps/', views.index, name='ps'),
    path('', views.index, name='index'),
    path('lms/read_pdf/', views.read_pdf, name='read_pdf'),


]
