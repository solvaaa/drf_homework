from django.urls import path
from rest_framework import routers

from courses.apps import CoursesConfig
from courses.views.lesson import *
from courses.views.course import *

appname = CoursesConfig.name

router = routers.DefaultRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = router.urls

urlpatterns += [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/edit/<int:pk>', LessonUpdateView.as_view(), name='lesson_edit'),
    path('lesson/delete/<int:pk>', LessonDestroyView.as_view(), name='lesson_delete'),
]


