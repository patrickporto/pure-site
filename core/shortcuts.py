from core.conf import settings
from jinja2 import Environment, PackageLoader


for app in settings.PROJECT_APPS:
    env = Environment(loader=PackageLoader(app, 'templates'))


def render(template_name, context={}):
    template = env.get_template(template_name)
    return str(template.render(**context))
