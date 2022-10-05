from django.shortcuts import render
from .forms import ContactForm
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
# Import render module
from django.shortcuts import render
from django.urls import reverse


#
#
# importing the required module
# import pdfkit
#
# # configuring pdfkit to point to our installation of wkhtmltopdf
# config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
#
# # converting html file to pdf file
# pdfkit.from_file('home.html', 'output.pdf', configuration=config)
# import pdfkit as pdf
# pdf.from_string('hello','string.pdf')
# pdf.from_file('home.html','file.pdf')
# url='https://en.wikipedia.org/wiki/QWERTY'
# pdf.from_url(url,'website.pdf')
#
# path_to_wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# url='https://wkhtmltopdf.org/'
# path_to_file='home.html'
# config=pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
# pdfkit.from_file(path_to_file,output_path='home.pdf',configuration=config)
# pdfkit.from_url(url,output_path='webpage.pdf',configuration=config)
#

# import os
# from django.conf import settings
# from django.http import HttpResponse, Http404

def home(request):
	return render(request, 'home.html', {})

def info(request):
	form=ContactForm()
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():

			name=form.cleaned_data['name']
			email=form.cleaned_data['email']

			skills_1=form.cleaned_data['skills_1']
			skills_2=form.cleaned_data['skills_2']
			skills_3=form.cleaned_data['skills_3']
			skills_4=form.cleaned_data['skills_4']

			mobile=form.cleaned_data['mobile']
			address=form.cleaned_data['address']

			experience_1_title=form.cleaned_data['experience_1_title']
			experience_1_dur=form.cleaned_data['experience_1_dur']
			experience_1_desc=form.cleaned_data['experience_1_desc']

			experience_2_title=form.cleaned_data['experience_2_title']
			experience_2_dur=form.cleaned_data['experience_2_dur']
			experience_2_desc=form.cleaned_data['experience_2_desc']

			education_1=form.cleaned_data['education_1']
			education_1_dur=form.cleaned_data['education_1_dur']
			education1_score=form.cleaned_data['education1_score']

			education_2=form.cleaned_data['education_2']
			education_2_dur=form.cleaned_data['education_2_dur']
			education2_score=form.cleaned_data['education2_score']
			#
			education_3 = form.cleaned_data['education_3']
			education_3_dur = form.cleaned_data['education_3_dur']
			education3_score = form.cleaned_data['education3_score']

			data={'name':name}
			data['email']=email
			data['skills_1']=skills_1
			data['skills_2']=skills_2
			data['skills_3']=skills_3
			data['skills_4']=skills_4

			data['mobile']=mobile
			data['address']=address

			data['experience_1_title']=experience_1_title
			data['experience_1_dur']=experience_1_dur
			data['experience_1_desc']=experience_1_desc

			data['experience_2_title']=experience_2_title
			data['experience_2_dur']=experience_2_dur
			data['experience_2_desc']=experience_2_desc

			data['education_1']=education_1
			data['education_1_dur']=education_1_dur
			data['education1_score']=education1_score

			data['education_2']=education_2
			data['education_2_dur']=education_2_dur
			data['education2_score']=education2_score
            # user=form.save()

			#
			#
			data['education_3']=education_3
			data['education_3_dur']=education_3_dur
			data['education3_score']=education3_score

			return render(request,'home.html',data)
			#to add more go to : forms.py
			# print(name,email)
	return render(request,'info.html',{'form':form})




#
# import os
# from django.conf import settings
# from django.http import HttpResponse, Http404
#
# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#     return response
#     raise Http404

# Import mimetypes module
# import mimetypes
# # import os module
# import os
# # Import HttpResponse module
# from django.http.response import HttpResponse

#
def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/resumesite/Files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'file.html')







from django.contrib.auth.models import User,auth,UserManager
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import get_object_or_404, render
# def login(request,user):
#     User=User.objects.create_user(username=username,email=email,password=password)
#     User.last_name="lennon"
#     User.save()
#     user = authenticate(username='john', password='secret')
#     if user is not None:
#         # A backend authenticated the credentials
#         auth.login(request,user)
#         return redirect("/home")
#     else:
#         messages.info(request, "invalid user")
#         return render(request, "busapp/login.html")
#         # No backend authenticated the credentials
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def homepage(request):
    return render(request,"homepage.html")

def signup(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=name,email=email,password=password,)
        if user:
            login(request,user)
            return render(request,'thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'signup.html', context)
    else:
        return render(request, 'signup.html', context)

def signin(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name,password=password)
        if user:
            login(request,user)
            # username = request.session['username']
            context["user"] = name
            context["id"] = request.user.id
            return render(request, 'success.html',context)
            return HttpResponseRedirect('success')
            return redirect("resume1")
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'signin.html',context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'signin.html',context)

def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'signin.html', context)

