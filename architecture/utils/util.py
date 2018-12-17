import inspect
import importlib

"""
Carrega um modulo dinamicamente do pacote forms
"""
def find_widget(widget_type):
    try:
        module = importlib.import_module('forms.{0}'.format(widget_type))

        for x in dir(module):
            
            if x == widget_type:
                obj = getattr(module, x)
                if inspect.isclass(obj):
                    return obj
    except ImportError:
        return None
