
import os, sys
sys.path.append(os.path.dirname(__file__))

import myapp, wsgi_coverage
wsgi_coverage.import_submodules(myapp)

import myapp.wsgi
application = wsgi_coverage.measured(myapp.wsgi.application)

