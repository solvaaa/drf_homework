from django.urls import path
from rest_framework import routers

from courses.apps import CoursesConfig
from courses.views.lesson import *
from courses.views.course import *
from courses.views.payment import *
from courses.views.subscription import SubscriptionCreateView, SubscriptionDeleteView

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
    path('payments/', PaymentListView.as_view(), name='payments'),
    path('course/<int:course_id>/subscribe/', SubscriptionCreateView.as_view(), name='subscribe'),
    path('course/<int:course_id>/unsubscribe/', SubscriptionDeleteView.as_view(), name='unsubscribe'),
    path('course/<int:course_id>/buy', PaymentPayView.as_view(), name='buy'),

]


