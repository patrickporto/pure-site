from wsgiref.simple_server import make_server
from wsgiref.util import shift_path_info


def dynamic_import(ref):
    ref_splited = ref.split('.')
    package = ".".join(ref_splited[:-1])
    name = ref_splited[-1]
    module = __import__(package, fromlist=[name])
    return getattr(module, name)


class App(object):
    def __init__(self):
        self.urls = {}

    def route(self, url):
        def wrapper(view):
            self.urls[url] = view
        return wrapper

    def __call__(self, environ, start_response):
        headers = []
        for middleware in self.settings.MIDDLEWARE_CLASSES:
            Middleware = dynamic_import(middleware)
            middleware_instance = Middleware(environ, start_response)
            if middleware_instance.is_valid():
                return middleware_instance.get_response()
        url = "/{0}".format(shift_path_info(environ))
        headers.append(('Content-type', 'text/html'))
        view = self.urls.get(url)
        if view:
            start_response("200 OK", headers)
            return view()
        start_response("404 Not Found", headers)
        return "Erro 404 - Page not found"

    def __setup(self):
        from core.conf import settings
        self.settings = settings

    def __load_views(self):
        for app in self.settings.PROJECT_APPS:
            __import__('{0}.views'.format(app))

    def run(self, host='127.0.0.1', port=8080):
        self.__setup()
        self.__load_views()
        server = make_server(host, port, self)
        server.serve_forever()

app = App()
