from flask import Flask
import logging
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    logging.basicConfig(filename='logs/app.log',
                        level=logging.DEBUG,
                        format='%(asctime)s --- %(levelname)s --- %(message)s'
                        )
    
    from app.routes import routes
    app.register_blueprint(routes)
    
    return app