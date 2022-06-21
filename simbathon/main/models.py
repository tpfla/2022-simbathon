from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    price = models.CharField(max_length=100, blank=False, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
# Create your models here.
