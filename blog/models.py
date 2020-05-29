from django.db import models
# import uuid

# Create your models here.
# id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

class Article(models.Model):
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='yazar')
   title = models.CharField(max_length=100)
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.title
      


# Notes
# on_delete=models.CASCADE => auth_user table'indaki user silindiginde o user'in article'larinida siler
# verbose_name='yazar' => admin panelini customize etmek icin. author yerine yazar gorunuyor.