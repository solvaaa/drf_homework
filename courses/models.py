from django.db import models

from users.models import NULLABLE, User


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, verbose_name='пользователь')
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                verbose_name='стоимость', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses",
                               verbose_name='курс', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, verbose_name='пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('course', 'name')


class Payment(models.Model):
    CASH = 'CASH'
    CREDIT = 'CREDIT'
    TYPE_CHOICES = (
        (CASH, 'наличные'),
        (CREDIT, 'безнал')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_payment = models.DateTimeField(verbose_name='дата оплаты')
    course = models.ForeignKey(Course, verbose_name='оплаченный курс',
                               on_delete=models.SET_NULL, **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='оплаченный урок',
                               on_delete=models.SET_NULL, **NULLABLE)
    total = models.FloatField(verbose_name='сумма оплаты')
    payment_type = models.CharField(max_length=20, choices=TYPE_CHOICES,
                                    verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} {self.total}'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    is_subscribed = models.BooleanField(default=True, verbose_name='подписан')

    def __str__(self):
        return f'{self.user} - {self.course} sub:{self.is_subscribed}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
