from django.shortcuts import render
from project_app.models import project
from contactus_app.models import Footer
from contactus_app.models import Message



def home(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        Message.objects.create(first_name=first_name, email=email, body=body, subject=subject )

    projects = project.objects.all()
    footer = Footer.objects.all().last()
    return render(request, 'index.html', context={'projects': projects, 'footer': footer})