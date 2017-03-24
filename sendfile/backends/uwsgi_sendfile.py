import uwsgi


def sendfile(request, filename, **kwargs):
    """
    Use uwsgi's sendfile implementation for answering the request
    :param request:
    :param filename:
    :param kwargs:
    :return:
    """
    return uwsgi.sendfile(filename)
