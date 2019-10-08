# The socket to bind.
bind = '127.0.0.1:8000'
# Max number of pending connections.
backlog = 1024
# Number of workers spawned for request handling.
workers = 1
# Standard type of workers.
worker_class = 'sync'
# Kill worker if it does not notify the master process in this number of seconds.
timeout = 30
# Log file location.
logfile = '/var/log/productcatalog-gunicorn.log'
# The granularity of log output.
loglevel = 'info'
