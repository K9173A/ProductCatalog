from .base import *


if os.environ.get('PROD_HEROKU'):
    from .prod_heroku import *
elif os.environ.get('PROD_LOCAL'):
    from .prod_local import *
elif os.environ.get('DEV'):
    from .dev import *
