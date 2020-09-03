# Websites

This exercise, we will be making a test website using Python.

Make sure to have Virtual Environment activated for all future exercises, it is extremely useful.

## Install Flask

First, a web framework named `flask` has to be installed.

The term ”framework” generally means ”some package that makes it easier for me to do something.”
In the world of web applications, people create ”web frameworks” to compensate for the difficult problems they have encountered when making their own sites. They share these common solutions in the form of a package you can download to bootstrap your own projects.

to install flask, make sure to be in the Virtual Environment. Execute the following command:

```bash
pip install flask
```

## How Flask Works

1. Your browser makes a network connection to your own computer, which is called `localhost` and is a standard way of saying ”whatever my own computer is called on the network.” It also uses `port 5000`.
2. Once it connects, it makes an HTTP request to the `app.py` application and asks for the `/` URL, which is commonly the first URL on any website.
3. Inside `app.py` you’ve got a list of URLs and what functions they match. The only one we have is the '/', 'index' mapping. This means that whenever someone goes to / with a browser, flask will find the `def index` and run it to handle the request.
4. Now that flask has found `def index`, it calls it to actually handle the request. This function runs and simply returns a string for what flask should send to the browser.
5. Finally, flask has handled the request and sends this response to the browser, which is what you are seeing.

## A Note on Debugger Mode

Debugger mode is a very helpful way for you to debug interactively and find errors. However, it is also very dangerous as it exposes an easy vulnerability to anyone on the website. Therefore, **never** *ever* use debugger mode when you are developing while connected to the internet.

To activate Debugger mode, execute the following.

```bash
export FLASK_DEBUG=1
```

## How (HTML) Templates Work
1. In your `app.py` you’ve imported a new function named `render_template` at the top.
2. This render_template knows how to load `.html` files out of the templates/directory because that is the default magic setting for a Flask application.
3. Later in your code, when the browser hits the def index, instead of just returning the string greeting , you call `render_template` and pass the greeting to it as a variable.
4. This `render_template` method then loads the `templates/index.html` file (even though you didn’t explicitly say templates ) and processes it.
5. In this `templates/index.html` file you have what looks like normal HTML, but then there’s ”code” placed between two kinds of markers. One is `{% %}` , which marks pieces of ”executable code” (if-statements, for-loops, etc). The other is `{{ }}` which marks variables to be converted into text and placed into the HTML output. The `{% %}` executable code doesn’t show up in the HTML. To learn more about this template language read the Jinja2 Documentation.

[Flask Documentation](http://flask.pocoo.org/docs/0.12/).

Note that Django is a more popular web-development language for Python. However, it takes more time for beginners to learn.
