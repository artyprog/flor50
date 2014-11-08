from django import template
import mako.template as mako
import subprocess
import sys

def do_mako(parser, token):
    nodelist = parser.parse(('endmako',))
    parser.delete_first_token()
    return makoNode(nodelist)
class makoNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        block = self.nodelist.render(context)
        #turn the context into a dict
        parameters = {}
        [parameters.update(parameter) for parameter in context]
        #render with Mako
        rendered = mako.Template(block, format_exceptions=True).render(**parameters)
        return rendered

def do_rapyd(parser, token):
    nodelist = parser.parse(('endrapyd',))
    parser.delete_first_token()
    return rapydNode(nodelist)

class rapydNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        block = self.nodelist.render(context)
        print(str(block))
        #turn the context into a dict
        parameters = {}
        [parameters.update(parameter) for parameter in context]
        #render with Mako
        rapydscript_path = '/tmp/hello.pyj'
        f = open(rapydscript_path, 'w')
        f.write(block); f.close()
        command = r'rapydscript %s -b -p'%(rapydscript_path)
        child = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        output,error = child.communicate()
        print(output)
        return output


register = template.Library()
register.tag('mako', do_mako)
register.tag('rapyd', do_rapyd)

