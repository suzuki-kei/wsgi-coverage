import coverage
import glob
import importlib
import os


def measured(target: callable) -> callable:
    def wrapper(*args, **kwargs):
        cov = _new_coverage()
        try:
            cov.start()
            return target(*args, **kwargs)
        finally:
            cov.stop()
            cov.save()
    return wrapper


def _new_coverage():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    config_file = os.path.join(root_dir, "config", "coveragerc")
    cov = coverage.Coverage(config_file=config_file)
    cov.load()
    return cov
    #return coverage.Coverage(config_file=config_file)


@measured
def import_submodules(module):
    files = glob.glob(os.path.join(os.path.dirname(module.__file__), '[a-zA-Z0-9]*.py'))
    names = [os.path.split(os.path.splitext(file)[0])[1] for file in files]
    submodules = [importlib.import_module('.'.join([module.__name__, name])) for name in names]
    return submodules

