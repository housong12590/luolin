from app.utils import SQLHelper

result = SQLHelper.fetch_one('select * from users', [])
print(result)

from werkzeug.wsgi import DispatcherMiddleware

from werkzeug.serving import run_simple

app = DispatcherMiddleware(None, {
    '/admin': None
})

run_simple('127.0.0.1', 5000, app, use_reloader=True, use_debugger=True)
