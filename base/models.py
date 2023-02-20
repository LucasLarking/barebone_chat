from django.db import models


class Room(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # Visa nyaste rummen först
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # Visa nyaste messagena först
    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return self.message
