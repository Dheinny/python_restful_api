# _*_ encode: utf-8 _*_

from mongoengine.errors import (
    DoesNotExist
)

from apps.responses import (
    resp_exception, resp_does_not_exist,
)


class GetDecorator(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        try:
            return self.f(*args, **kwargs)

        except DoesNotExist as e:
            return resp_does_not_exist("Resource", "resource {} {}".format(*(kwargs.popitem())))

        except Exception as e:
            return resp_exception("Resource", description=e.__str__())


class DeleteDecorator(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        try:
            return self.f(*args, **kwargs)

        except DoesNotExist as e:
            return resp_does_not_exist("Resource", "resource {} {}".format(*(kwargs.popitem())))

        except Exception as e:
            return resp_exception("resource", description=e.__str__())




