from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Article(models.Model):
    """
    An abstract base class to allow a user to create and publish their own articles.

    YOU WILL NEED TO SET THE article_author FOREIGN KEY YOURSELF!
    """
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField(max_length=500)
    keywords = models.CharField(max_length=250)
    slug = models.SlugField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Job(Article):
    """
    A model built on the Article abstract base class to allow companies and recruiting agents
    to create and publish employment listings. Tracks the number of candidates that have applied
    to the listing.

    YOU WILL NEED TO SET THE for_company FOREIGN KEY YOURSELF!
    """
    position_title = models.CharField(max_length=150)
    company = models.CharField(max_length=250)  # TODO come back later to set as a foreign key field
    location = models.CharField(max_length=250)
    description = RichTextField(max_length=3000)
    requirements = models.TextField(max_length=3000)
    benefits = RichTextField(max_length=3000)
    others = models.BooleanField(default=False)
    other = RichTextField(max_length=3000, blank=True)
    remote = models.BooleanField(default=False)
    candidates = models.IntegerField(default=0)
    closed = models.BooleanField(default=False)
    datetime_closed = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.position_title} by {self.company}"

    def save(self, *args, **kwargs):
        """Create the slug field at creation of new Job."""
        slug = str(self.datetime) + '-' + str(self.company)  # TODO change slug to generate unique text per Job
        self.slug = slugify(slug)
