from jinja2 import Environment, FileSystemLoader

from framework.settings import TEMPLATES_PATH


def render(template_name, **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(TEMPLATES_PATH)
    template = env.get_template(template_name)
    return template.render(**kwargs)
