import os

from app import create_app

# config_name = os.getenv('FLASK_ENV')
# app = create_app(config_name)

app = create_app()

if __name__ == '__main__':
    app.run(port=5000)