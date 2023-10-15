from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field).lower()
        if tmp_value.find('youtube') == -1:
            raise ValidationError('Link is not an youtube video')
