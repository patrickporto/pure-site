from core.http import Response
from wsgiref.util import request_uri
import re
import os
import mimetypes

mimetypes.init()

class StaticMiddleware(object):
    def __init__(self, environ, start_response):
        from core.conf import settings
        self.static_url = settings.STATIC_URL
        self.apps = settings.PROJECT_APPS
        self.regex = re.compile("{0}(?P<filename>.*)".format(self.static_url))
        self.environ = environ
        self.start_response = start_response

    def is_valid(self):
        url = request_uri(self.environ)
        filename = self.regex.search(url)
        if filename:
            for app in self.apps:
                path = '{0}/{1}'.format(app, filename.group(0))
                if os.path.exists(path):
                    self.path = path
                    return True
        return False

    def get_response(self):
        file = open(self.path, 'r')
        content = file.read()
        file.close()
        extension = '.{0}'.format(self.path.split('.')[-1])
        response = Response(content, mimetypes.types_map[extension])
        self.start_response("200 OK", response.headers)
        return response.content
