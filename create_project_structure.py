import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content='', source_path=None):
    if source_path:
        with open(source_path, 'r') as f:
            content = f.read()
    with open(path, 'w') as f:
        f.write(content)

def main():
    # Project root
    root_dir = './'
    os.chdir(root_dir)

    # Directory structure
    dirs = [
        'src',
        'src/templates',
        'src/static',
        'src/static/css',
        'src/static/js',
        'src/llm',
        'src/routes',
        'src/utils'
    ]

    for dir in dirs:
        create_directory(dir)

    # Create files
    create_file('src/__init__.py', '''from flask import Flask

app = Flask(__name__)

from src import routes
''')
    create_file('src/routes/routes.py', '''from flask import render_template
from src import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
''')
    create_file('src/templates/index.html', '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - AI Report Generator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>
    <header>
        <h1>Title</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Footer</p>
    </footer>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
''')
    create_file('src/templates/base.html', '''
{% extends "index.html" %}

{% block content %}
    <h2>Subtitle</h2>
    <div id="abc">
        <!-- abc form will go here -->
    </div>
{% endblock %}
''')
    create_file('src/static/css/main.css', '/* Main CSS styles will go here */')
    create_file('src/static/js/main.js', '// Main JavaScript code will go here')
    create_file('src/llm/__init__.py')
    create_file('src/utils/__init__.py')
    create_file('config.py', '''import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Add other configuration variables here
''')
    create_file('run.py', '''from src import app

if __name__ == '__main__':
    app.run(debug=True)
''')
    create_file('requirements.txt', '''
flask
''')
    create_file('.gitignore', '''
*.pyc
__pycache__/
venv/
.env
.pytest_cache/
''')

    # Load specific files from C:/Code/Utils and save them in the project structure
    create_file('src/.env', source_path='C:/Code/Utils/.env')
    create_file('src/llm/llm_config.py', source_path='C:/Code/Utils/llm_config.py')

if __name__ == "__main__":
    main()