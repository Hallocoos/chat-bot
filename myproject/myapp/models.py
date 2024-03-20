from django.db import models


class Conversation(models.Model):
    userid = models.CharField(max_length=100)
    conversationid = models.CharField(max_length=100)
    optionpicked = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        app_label = "myapp"

    def __str__(self):
        return f"Conversation {self.conversationid} - User {self.userid}"
