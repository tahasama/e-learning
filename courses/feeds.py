from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Course


class CourseFeed(Feed):
    title = 'Courses'
    link = reverse_lazy('course_list')
    description = 'New courses on the platform.'

    def items(self):
        return Course.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.overview, 30)


    