##Django Accounts App
A sample app that managed multiple accounts and their transactions


### Requirements

* Python 3 (I used 3.5.0)
* Django 1.9.x

### Setting Up

Install the dependencies first:

	pip install -r requirements.txt

The default settings uses a SQLite database. So you can just run the migrations and run the server straight away:


	python manage.py migrate
	python manage.py runserver
	

#### Using MySQL (Optional)	

If you would like to use MySQL, the `requirements.txt` file also installs the MySQL driver for you. So you can easily switch to MySQL by editing the `settings.py`. 

For MySQL, the `DATABASES` section should look like this: 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'badku',
        'USER': 'root',
        'PASSWORD': 'masnun',
        'HOST': '127.0.0.1',
    }
}
```

If you want to use other database backends, you will need to manually install the driver and change the settings.