from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    username = models.CharField(max_length=300, blank=False, null=False)
    phone_number= models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField("Create time", auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.id} || {self.name} || {self.phone_number}"


class Post(models.Model):
    title = models.CharField(max_length=300)
    body  = models.TextField()
    url_name = models.URLField(max_length=400)
    image = models.ImageField(upload_to='photos/', verbose_name='rasm')
    create  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}  || {self.body}"


    def get_absolute_url(self):
        return "/"  + str(self.id)  + "/"


    # def get_absolute_url(self):
    #     return reverse('post', kwargs = {'post_id': self.pk})


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['title', 'body']

