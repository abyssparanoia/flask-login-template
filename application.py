from app import app
app.run()

'''
基本的にこのファイルは鯖側でのトリガーとする。
elastic beanstalkがapplication.pyをデフォルトで認識するのでファイル名をこれにしています
ファイル構成はこのような感じです。

.
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-36.pyc
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── forms.cpython-36.pyc
│   │   │   └── user.cpython-36.pyc
│   │   ├── forms.py
│   │   └── user.py
│   ├── templates
│   │   ├── base.html
│   │   ├── flash.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── settings.html
│   │   └── write.html
│   └── views
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-36.pyc
│       │   ├── home.cpython-36.pyc
│       │   ├── login.cpython-36.pyc
│       │   ├── logout.cpython-36.pyc
│       │   └── write.cpython-36.pyc
│       ├── home.py
│       ├── login.py
│       ├── logout.py
│       └── write.py
├── application.py
├── config.py
└── requirements.txt

'''
