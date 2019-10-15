import os


if os.environ.get('PROD_HEROKU'):
    from .prod_heroku import *
elif os.environ.get('PROD_LOCAL'):
    from .base import *
    from .prod_local import *
else:
    from .base import *
    from .dev import *
