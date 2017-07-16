# SimpleDjangoBlog

> A simple blog using minimal Python and Django


## Install

#### python

Using the system Python can be dangerous for Python development. If you would like to install a
standalone version of Python please follow the guide below.

* Python 2.7
    - http://docs.python-guide.org/en/latest/starting/install/osx/#doing-it-right

#### pip

**Note:** pip may be installed along with Python. 

Pip can be installed by running

```
$ python get-pip.py
```

I used an earlier version of pip, so you may need to downgrade.

```
$ pip install pip==1.5.6
```

##### virtualenv

For Python development, we highly recommend using a [virtual environment
(virtualenv)](http://www.virtualenv.org/en/latest/) to ease development.

Install virtualenv with pip

```
$ [sudo] pip install virtualenv
```

Once install create a new virtualenv and activate it. 

```
$ mkvirtualenv blog -a $PWD 
$ workon blog # Activate the virtualenv
```

### requirements

Finally we just need to install the requirements.

```
$ pip install -r requirements.txt
```
