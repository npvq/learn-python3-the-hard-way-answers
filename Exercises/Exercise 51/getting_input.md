# Getting Input from a Browser

This exercise we will improve on our "Hello World" by using forms and storing information about users into their ”sessions.”

![alt-text: Diagram](How%20The%20Internet%20Works.png "How The Internet Works")

1. You type in the url `http://test.com//` into your browser, and it sends the request on line (A) to your computer’s network interface.
2. Your request goes out over the internet on line (B) and then to the remote computer on line (C) where my server accepts the request.
3. Once my computer accepts it, my web application gets it on line (D), and my Python code runs the index.GET handler.
4. The response comes out of my Python server when I return it, and it goes back to your browser over line (D) again.
5. The server running this site takes the response off line (D), then sends it back over the internet on line (C).
6. The response from the server then comes off the internet on line (B), and your computer’s network interface hands it to your browser on line (A).
7. Finally, your browser then displays the response.


In this description there are a few terms you should know so that you have a common vocabulary to work with when talking about your web application:

- **Browser** The software that you’re probably using every day. Most people don’t know what a browser really does. They just call browsers ”the internet.” Its job is to take addresses (like `http://test.com/`) you type into the URL bar, then use that information to make requests to the server at that address.
- **Address** This is normally a URL (Uniform Resource Locator) like `http://test.com//` and indicates where a browser should go. The first part, http , indicates the protocol you want to use, in this case ”Hyper- Text Transport Protocol.” You can also try ftp://ibiblio.org/ to see how ”File Transport Protocol” works. The `http://test.com/` part is the ”hostname,” a human readable address you can remember and which maps to a number called an IP address, similar to a telephone number for a computer on the internet. Finally, URLs can have a trailing path like the /book/ part of `http://test.com//book/`, which indicates a file or some resource on the server to retrieve with a request. There are many other parts, but those are the main ones.
- **Connection** Once a browser knows what protocol you want to use (http), what server you want to talk to (`http://test.com/`), and what resource on that server to get, it must make a connection. The browser simply asks your operating system (OS) to open a ”port” to the computer, usually port 80. When it works, the OS hands back to your program something that works like a file, but is actually sending and receiving bytes over the network wires between your computer and the other computer at `http://test.com/`. This is also the same thing that happens with `http://localhost:8080/`, but in this case you’re telling the browser to connect to your own computer (localhost) and use port 8080 rather than the default of 80. You could also do `http://test.com:80/` and get the same result, except you’re explicitly saying to use port 80 instead of letting it be that by default.
- **Request** Your browser is connected using the address you gave. Now it needs to ask for the resource it wants (or you want) on the remote server. If you gave /book/ at the end of the URL, then you want the file (resource) at /book/ , and most servers will use the real file /book/index.html but pretend it doesn’t exist. What the browser does to get this resource is send a request to the server. I won’t get into exactly how it does this, but just understand that it has to send something to query the server for the request. The interesting thing is that these ”resources” don’t have to be files. For instance, when the browser in your application asks for something, the server is returning something your Python code generated.
- **Server** The server is the computer at the end of a browser’s connection that knows how to answer your browser’s requests for files/resources. Most web servers just send files, and that’s actually the majority of traffic. But you’re actually building a server in Python that knows how to take requests for resources and then return strings that you craft using Python. When you do this crafting, you are pretending to be a file to the browser, but really it’s just code. As you can see from Exercise 50, it also doesn’t take much code to create a response.
- **Response** This is the HTML (CSS, JavaScript, or images) your server wants to send back to the browser as the answer to the browser’s request. In the case of files, it just reads them off the disk and sends them to the browser, but it wraps the contents of the disk in a special ”header” so the browser knows what it’s getting. In the case of your application, you’re still sending the same thing, including the header, but you generate that data on the fly with your Python code.


That is the fastest crash course in how a web browser accesses information on servers on the internet. It should work well enough for you to understand this exercise, but if not, read about it as much as you can until you get it. A really good way to do that is to take the diagram and break different parts of the web application you did in Exercise 50. If you can break your web application in predictable ways using the diagram, you’ll start to understand how it works.


## Changes Made to the Form

1. Instead of just a string for greeting , I’m now using `request.args` to get data from the browser. This is a simple dict that contains the form values as `key=value` pairs.
2. I then construct the greeting from the new name , which should be very familiar to you by now.
3. Everything else about the file is the same as before.

## How POST Forms Work

`<form action="/hello" method="POST">` tells your browser to:
1. Collect data from the user using the form fields inside the form.
2. Send them to the server using a POST type of request, which is just another browser request that ”hides” the form fields.
3. Send that to the /hello URL (as shown in the action="/hello" part).

You can then see how the two <input> tags match the names of the variables in your new code. Also notice that instead of just a GET method inside class index , I have another method, POST. How this new application works is as follows:

1. Your request goes to index() like normal, except now there is an if-statement that checks the request.method for either "POST" or "GET" methods. This is how the browser tells app.py that a request is either a form submission or URL parameters.
2. If request.method is "POST" , then you process the form as if it were filled out and submitted, returning the proper greeting.
3. If request.method is anything else, then you simply return the hello_form.html for the user to fill out.
