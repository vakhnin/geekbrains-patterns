import os

from jinja2 import Template

from framework.settings import TEMPLATES_PATH


def render(template_name, **kwargs):
    template_name = TEMPLATES_PATH + os.sep + template_name
    with open(template_name, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
