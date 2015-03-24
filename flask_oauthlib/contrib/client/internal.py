__all__ = ['RequestTermination']


class RequestTermination(Exception):
    """This exception should be raised while ``errorhandler`` was called and
    returned a response object.

    :param response: a response object.
    :type response: :class:`werkzeug.wrappers.Response`
    """
