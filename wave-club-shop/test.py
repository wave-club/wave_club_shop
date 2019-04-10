    # mysite_uwsgi.ini file
    [uwsgi]

    # Django-related settings
    # the base directory (full path)
    chdir           = /home/learn/python/website/wave-club-shop
    # Django's wsgi file
    module          = MxOnline.wsgi
    # the virtualenv (full path)

    # process-related settings
    # master
    master          = true
    # maximum number of worker processes
    processes       = 10
    # the socket (use the full path to be safe
    socket          = 127.0.0.1:8000
    # ... with appropriate permissions - may be needed
    # chmod-socket    = 664
    # clear environment on exit
    vacuum          = true
    virtualenv = /home/bobby/.virtualenvs/mxonline

    logto = /tmp/mylog.log