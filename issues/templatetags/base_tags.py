from django import template
from django.template import Variable, VariableDoesNotExist
register = template.Library()
 
@register.filter
def gVal(object, attr):
    """Check the array, dict, etc for a value"""
    quasai = { 'object' : object }
    #print "gVal :: " + str(attr) +" - "+ str(quasai)
    try:
        value = Variable('object.%s' % attr).resolve(quasai)
    except VariableDoesNotExist:
        value = None
    return value

 
@register.filter
def xVal(a,b):
    """Since Python resolves left to right in template tags: pass value and then the dick to check; returns value or 0"""
    #print "xVal",a,b
    if b.has_key(a):
        value = b[a]
    else:
        value = "0"
    return value 


def checkbox_ajax(id,type):
    """Takes an issue ID and the type of checkbox and sends the command to toggle it!"""
    
    rtn_str = "<input type='checkbox' name='"+id+"-"+box+"' id='"+id+"-"+box+"' onClick='javascript:toggle_status('"+id+"','"+box+"')' />"
    return rtn_str