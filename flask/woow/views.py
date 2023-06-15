from django.shortcuts import render, redirect
from .models import Customer, Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import DetailView
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.template.loader import render_to_string
import csv



def Index(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('conform.html',{
                'name':name, 'email':email,
                'content':content})
            print(html)
            send_mail('This is subject','This is the message','burhonabdullayev7@gmail.com',['buymax586@gmail.com'],html_message=html)
            return redirect('home')

    else:
        form = ContactForm()


    return render(request, 'home.html',  {'form':form})

# def send(request):
#     send_mail('contact mail','hello guys',
#               'burhonabdullayev7@gmail.com'
#             ,['buymax586@gmail.com']
#                    ,fail_silently=False)
#     return render(request, 'home.html')

# def Home(request):
#     if request.method =="POST":
#         message = request.POST['message']
#         send_mail('Contact Form', message,
#                   settings.EMAIL_HOST_USER,
#                   ['akbarovamaxmuda662@gmail.com'],
#                   fail_silently=False)
#     return render(request, 'home.html')


# def export_csv(request):
#     students=User.objects.all()
#     response=HttpResponse('text/cvs')
#     response['Content-Disposition'] = 'attachment; filename=export_csv' + str(datetime.now()) + '.csv'
#
#     write=csv.writer(response)
#     write.writerow([ 'id',  'name', "username", "phone_number", "message", "create_at"])
#     students_fields=students.values_list('id', 'name', 'username', "phone_number", "message", "create_at")
#     for student in students_fields:
#         write.writerow(student)
#     return response

def Post_today(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Post.objects.all().filter(Q(title__icontains=q)|Q(body__icontains=q))
    else:
        articles = Post.objects.all().order_by('-id')
        q = None
    return render(request, 'post.html', {"articles": articles, "q": q})



class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = 'a'



def user_page(request):
    if request.method == "POST":
        model = Customer()
        model.name = request.POST.get("name")
        model.username = request.POST.get("username")
        model.phone_number = request.POST.get("phone_number")
        model.message = request.POST.get("message")

        model.save()
        return render(request, "index.html")

    else:
        return render(request, "index.html")


def show_page(request, post_id):
    return HttpResponse(f"New post for all : {post_id}")




