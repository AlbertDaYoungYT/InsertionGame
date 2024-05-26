import os
import importlib

imported_modules = []
current_directory = os.path.dirname(__file__)

for filename in os.listdir(current_directory):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]
        importlib.import_module(f".{module_name}", package=__name__)

def run(_self):
    for module in imported_modules:
        if hasattr(module, '_import') and callable(getattr(module, '_import')):
            module._import(_self)