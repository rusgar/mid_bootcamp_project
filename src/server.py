from app import app
from controllers.ruta import *

app.run("0.0.0.0", "4500", debug=True)