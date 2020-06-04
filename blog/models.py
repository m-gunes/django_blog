from django.db import models
from ckeditor.fields import RichTextField
# import uuid

# Create your models here.
# id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

class Article(models.Model):
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='yazar')
   title = models.CharField(max_length=100)
   content = RichTextField() # for ckeditor
   # content = models.TextField()
   image = models.ImageField(upload_to='images/',null=True, blank = True, verbose_name='Add Photo')
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self): # Admin panelde title ile gostermek icin
      return self.title
   class Meta:
      ordering = ['-created_at']
      

class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_list')
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   # author = models.CharField(max_length=150)
   content = models.TextField(max_length=5000)
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.content
   class Meta:
      ordering = ['-created_at']


# Notes
# on_delete=models.CASCADE => auth_user table'indaki user silindiginde o user'in article'larinida siler
# verbose_name='yazar' => admin panelini customize etmek icin. author yerine yazar gorunuyor.
# ordering = ['-created_at'] descending order. son eklenen ilk basta
# ordering = ['created_at'] ascending order.