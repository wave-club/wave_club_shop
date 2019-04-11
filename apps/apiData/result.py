from django.http import JsonResponse
from apiData.code import Code


class Result(object):
    def __init__(self, code, message=None, data=None):
        self.code = code
        self.message = message
        self.data = data


    @staticmethod
    def success(data=None):
        return Result(Code.OK.value, data=data).to_dict()

    @staticmethod
    def error(code=Code.COMMON_ERROR.value, message=None):
        return Result(code, message).to_dict()

    def to_dict(self):
        result = {}

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.data is not None:
            result['data'] = self.data

        return JsonResponse(result)