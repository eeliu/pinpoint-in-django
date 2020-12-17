# pinpoint-in-django

### Download pinpoint-py-plugins
[pinpoint-py-plugins](https://github.com/pinpoint-apm/pinpoint-c-agent/releases/download/V2020.12.17/pinpoint-python-plugins-v0.0.1.tar.gz)


### Steps
1. copy pinpoint
2. enable pinpoint middleware
    ```py
     MIDDLEWARE = [
    'pinpoint.Django.DjangoMiddleWare',
    ...
    ]
    ```

3. run "python manage.py runserver"
