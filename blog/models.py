from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    judul  = models.CharField(max_length=255)
    body   = models.TextField() 
    catagory = models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now = True)
    slug = models.SlugField(blank=True, editable=False)
    get_latest_by = "order_date"

    def save(self):
        self.slug = slugify(self.judul)
        super(Post,self).save()


    def __str__(self):
        return "{},{}".format(self.id, self.judul)