"""
this script allow launch server quickly

```
    python run.py
```
"""


from __future__ import absolute_import
import os
import sys
# add parent folder as module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from project1.srv.api import app, sql

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

    # TODO: find a better place to create tables
    sql.create_all()

    app.run(
        port=9001,
        use_debugger=False,
        use_reloader=False
    )

