from __future__ import absolute_import
from project1.srv.rest import app

if __name__ == "__main__":

    """
    init static files.

    In production, serving static-files is done by nginx.

    The reason that we didn't utilize 'static_folder' and 'static_url_path'
    is these two parameters are only used in Flask.__init__, this is
    not capable in our case.
    """
    from os.path import join, dirname, abspath
    from werkzeug import SharedDataMiddleware

    app.wsgi_app = SharedDataMiddleware(
        app.wsgi_app,
        {
            '/': join(join(join(abspath(dirname(__file__)), 'client'), 'web'), 'app')
        }
    )

    app.run(
        port=9001,
        use_debugger=False,
        use_reloader=False
    )

