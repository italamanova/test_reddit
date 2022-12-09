from django.db import models
from django.utils import timezone


class Link(models.Model):
    created = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200)
    upvotes = models.PositiveSmallIntegerField(default=0)
    downvotes = models.PositiveSmallIntegerField(default=0)
    score = models.IntegerField(default=0)

    def upvote(self):
        self.upvotes += 1
        self.save()

    def downvote(self):
        self.downvotes += 1
        self.save()

    def save(self, *args, **kwargs):
        self.score = self.upvotes - self.downvotes
        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
