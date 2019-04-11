from django.http import JsonResponse

from code import Code


class CustomError(Exception):
    def __init__(self, code=Code.COMMON_ERROR.value, error='系统繁忙，请稍后再试'):
        super(CustomError, self).__init__()
        self.code = code
        self.error = error

    def to_dict(self):
        return JsonResponse({
            'code': self.code,
            'error': self.error
        })