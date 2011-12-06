from django import template
from django.template.defaulttags import CommentNode

register = template.Library()
def commen5(parser, token):
    """  
    Ignores everything between ``{% commen5 %}`` and ``{% endcommen5 %}``.
    """
    parser.skip_past('endcommen5')
    return CommentNode()
commen5 = register.tag(commen5)
