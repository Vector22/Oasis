# Oasis
A social website application with some basics to advanced features build in Django.

# Overview

## I. Why this project
## II. Application features
## III. Run the app
## IV. How it work
## V. Final words


# I. Why this project
This project is above all an expression of my freedom to code. Formatting ideas for modest applications is something I really love. It is also a way to assess my level of competence in Python3 / Django & JavaScript.
Not to mention that it's a good way (I think) to attract recruiters to the skills that I highlight in my job searches.


# II. Application features
This small application has been developed with followings technologies:
* Python v3.7
* Django v2.2
* JavaScript
* jQuery

And the features highlighted are:
* An authentication system for users to register, log in, edit their profile, and
change or reset their password.
* A followers' system to allow users to follow each other.
* A functionality to display shared images and implement a bookmarklet for users
to share images from any website.
* An activity stream for each user that allows users to see the content uploaded by
the people they follow.


# III. Run the app
> Please not that i use virtualenv to isolate python libraries; virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

### 1. Clone the repository

In the command prompt type:

    git clone https://github.com/Vector22/Oasis.git

Once this operation is complete, go to the root repository of the app by typing:

    cd oasis

### 2. Project structure
Inside the root directory of the project you'll have something like that. Don't worries about the **.json** files; they are just there for the code editor config to better track JavaScript errors with [Eslint](https://eslint.org/).

    .
    ├── django
    │   ├── account
    │   ├── actions
    │   ├── common
    │   ├── config
    │   ├── images
    │   ├── manage.py
    │   ├── media
    │   ├── static
    │   └── templates
    ├── package.json
    ├── package-lock.json
    ├── README.md
    └── requirements.txt

> Note that some others files or directories can be created after by lunching some command to setup the app or by uploading some images.
Also, the organization of the directories is a bit unusual, compared to the structure of a  standart Django project. This one is better suited for separate the backend code (If it was a API for example) from the front end code that is generaly done in HTM/JS.

### 3. Create a virtual environment

Let's now create an environment to isolate all the required package for run this application.

I'm using ***python virtualenv***, but many others are also good like [pyenv](https://github.com/pyenv/pyenv) or [pipenv](https://pipenv-fork.readthedocs.io/en/latest/).

I assume that you are in the **oasis** directory.
In the command prompt type:

    virtualenv -p python3 env
This command create a virtual environment named *env* with python3 as python version.

After that, you need to activate it by typing:

    source env/bin/activate

An example is:

    v3ct0r22@Ulrich:~/Django/Oasis$ source env/bin/activate
    (env) v3ct0r22@Ulrich:~/Django/Oasis$ 

### 4. Install the required packages

Now that you are in the virtual environment.
Let's install the packages required for the app.

    pip install -r requirements.txt

The command above can take a wile, depending on your internet connection and the computer speed so... You can take a small cofee cup ;-)

### 5. Run the migration

The title is a bit strange for people who are not familiar with Django or other python ORM usage.
For doing simple, the command sync the database with the models of the default applications
included in the INSTALLED_APPS setting(**django/config/settings.py**). And normaly must create a file like **db.sqlite3** in the **django** folder.
Since i used sqlite3 as database engine.

    cd django // since migration folder are there

And

    python manage.py migrate

You will see that all initial Django database migrations get applied and the defined models too.

### 6. Last step: fire up the server

Ok ok... It's well done now, apart from run the server and see how the app work.
Still in the **django** folder,

    python manage.py runserver

and point your browser to `http://localhost:8000/account/login/` since you need to login/register first before doing something.


# IV. How it work

### 1. Login/Register

The precedent link: `http://localhost:8000/account/login/` send you on the login page. Then you must to register first if it's your first time or login if you have already create an account.

### 2. Bookmark It
We assume that the django dev server is up and runing. If not, go in the django directory and type: 

    python manage.py runserver


* #### Run the app over ***https***
    You will need to be able to load the bookmarklet on any site, including sites served throughHTTPS. SSL has become widely used, and most websites serve content through HTTPS nowadays. For security reasons, your browser will prevent you from running the
    bookmarklet over HTTP on a site served through HTTPS.

* #### Ngrok
    The Django development server is intended only for development and doesn't support
    HTTPS. To test the bookmarklet over HTTPS, we will use Ngrok. Ngrok is a tool that
    creates a tunnel to expose your localhost to the internet through HTTP and HTTPS.

    Download Ngrok for your operating system from https://ngrok.com/download and run it
    from the shell using the following command:

        ./ngrok http 8000
    
    With the preceding command, you tell Ngrok to create a tunnel to your localhost on
    the 8000 port and assign an internet-accessible hostname for it. You should see an output
    similar to this one:

    
    Web Interface http://127.0.0.1:4040
    Forwarding http://3f6ad53c.ngrok.io -> localhost:8000
    Forwarding https://3f6ad53c.ngrok.io -> localhost:8000
    
    Ngrok tells us that our site, running locally at localhost on the 8000 port using Django's
    development server, is made available on the internet through
    the http://3f6ad53c.ngrok.io and https://3f6ad53c.ngrok.io URLs using the HTTP and HTTPS protocols, respectively.

    Edit the settings.py file of your project and add the host provided by Ngrok to the
    ALLOWED_HOSTS setting, as follows:

    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
        '3f6ad53c.ngrok.io'
    ]

    This will allow you to serve the application through the new hostname. Then, open the
    URL https://3f6ad53c.ngrok.io/account/login/ in your browser, replacing the
    host with the one provided by Ngrok. You will be able to see the login site.

    Edit the `bookmarklet_launcher.js` template and replace the http://127.0.0.1:8000/ URL with the HTTPS URL provided by Ngrok, as follows:
    `document.body.appendChild(document.createElement('script')).src='https://3f
    6ad53c.ngrok.io/static/js/bookmarklet/...'`

    Edit the js/bookmarklet.js static file, and take a look at the following line:
    `var site_url = 'http://127.0.0.1:8000/';`
    replace it by:
    `var site_url = 'https://3f6ad53c.ngrok.io/';`

* ### Do it now
    Open https://3f6ad53c.ngrok.io/account/.
    
    Once you successfully logged in, you can now bookmark an image by, first paste the **Bookmark it** button in your browser bookmark bar; and then go to any sites with some images (png/jpeg) like [this site](https://voyagerloin.com/post/75-photos-du-monde-lavez-jamais-vu) and click on the bookmartit button you just added in bar. Add  a name and a description to save. it's all. You can also see the others users actions like folowing and like some bookmarked images.


# V. Final words

The app is still in development and all the bugs and issues can be sended to [vector22dev@gmail.com]()

Thanks for trying to run my app and don't forget to contact me in the case you want learn more about me... \0/