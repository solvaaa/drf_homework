from django.urls import path
from rest_framework import routers

from courses.apps import CoursesConfig
from courses.views.lesson import *
from courses.views.course import *

appname = CoursesConfig.name

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonListView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>', LessonUpdateView.as_view(), name='lesson_edit'),
    path('lesson/delete/<int:pk>', LessonDestroyView.as_view(), name='lesson_delete'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls