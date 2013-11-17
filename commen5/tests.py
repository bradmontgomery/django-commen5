from django.template import Context, Template
from django.test import TestCase


class TestTemplateTags(TestCase):

    def test_commen5(self):

        template = Template(
            "{% load commen5_tags %}"
            "<html>{% commen5 %}LOL, NO{% endcommen5 %}</html>"
        )
        context = Context({})
        self.assertEqual(template.render(context), u"<html></html>")
