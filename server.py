from app import app

import os


PORT = int(os.environ.get('FLASK_SERVER_PORT', '8080'))

app.run(port=PORT)
