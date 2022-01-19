from django.db import models


class Poll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='polls', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
