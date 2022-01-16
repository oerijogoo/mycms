from django.db import models
from twilio.rest import Client
# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'AC71e61da13dbfc0f268376e124b666b5c'
            auth_token = '4d963576aa7ff60938460f3cec4ac4f2'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=f"Conrats {self.name}, your score is {self.score}",
                    from_='+17407594036',
                    to='+254725129000'
                        )
        else:
            account_sid = 'AC71e61da13dbfc0f268376e124b666b5c'
            auth_token = '4d963576aa7ff60938460f3cec4ac4f2'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=f"sorry {self.name}, your score is {self.score} . Try again",
                    from_='+17407594036',
                    to='+254725129000'
                 )

            print(message.sid)
        return super().save(*args, **kwargs)
