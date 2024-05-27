from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name="tweets", on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(verbose_name="Escreva aqui", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    # deadline = models.DateTimeField(verbose_name="Data de entrega", null=False, blank=False)
    # finished_at = models.DateTimeField(null=True)
    likes = models.ManyToManyField(User, related_name="tweet_like", blank=True)

    def like_amount(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created_at"]
