from core.base import app
from views import *  # NOQA
import os

os.environ.setdefault('SETTINGS_MODULE', 'config.settings')

app.run(host='0.0.0.0', port=80)
