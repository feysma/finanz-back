from importlib import import_module

modules = [module for module in __path__ if hasattr(module, '__package__')]
for module in modules:
    package_name = module.__name__.rsplit('.', 1)[0]
    package_path = package_name.replace('.', '/')
    sys.path.insert(0, package_path)
