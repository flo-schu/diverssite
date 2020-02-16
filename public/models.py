from django.conf import settings
from django.db import models
from django.utils import timezone


page_choice = (
    ('home','Home'),
    ('events','Events')
)

vis_choice = (
    ('public', 'Public'),
    ('members', 'Members')
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    page = models.CharField(max_length=50, null=True, choices=page_choice)
    text = models.TextField()
    visibility = models.CharField(max_length=20, default = "public",
                                  choices = vis_choice)
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True, verbose_name = "published")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title