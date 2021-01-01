from django.contrib.auth import get_user_model
from django.db import models
from courses.models import Course
from django.db.models.signals import post_save

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User,related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,blank=True, null=True, related_name='course_messages', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

    # @property
    # def room_group_name(self):
    #     return f'chat_{self.course.title}'

# def save_messages(self):
#     text_data_json = json.loads(text_data)
#     message = text_data_json['message']
#     course = get_object_or_404(Course,id=self.id)
#     messages = Message.objects.create(author=self.scope['user'], content=message,course=course)

def clear(sender, **kwargs):
    all_messages = Message.objects.all().count()
    if all_messages > 2000 :
        f = Message.objects.order_by('timestamp')
        f.first().delete()
    
post_save.connect(clear,sender=Message)  