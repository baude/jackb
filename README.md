# jackb

Collaborative project to implement a REST-based flask backend and web server GUI



## Backend setup

### Install the flask framework

```
# sudo apt-get install flask
```

### First time clone of a git repository

```
# git clone -a https://github.com/baude/jackb
```

The cloned code is now in the directory *jackb*.

### Updating an existing git repository

From within the directory where you have cloned.

```
# git pull
```

### Running the flask backend

From the *jackb* directory, issue the following command

```
# python backend/backend.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 Note the output from the python command.  The feedback here is that the flask service is now running
  on 127.0.0.1 (also known as localhost).  'localhost' is not routable, meaning you cannot use a different
  computer to get to that address.
  
### Verifying the flask service

I have set up two basic 'endpoints' that the flask service will respond to initially.  The more simple of
the two is the 'hello' endpoint.  We can use curl, a command line http browser, to check it:

```
# curl http://127.0.0.1:5000/hello
Hello from flask
# 
```

The second endpoint shows how we can use a variable from the URL given and do something with it.

```
# curl http://127.0.0.1:5000/hello/beavis
<!doctype html>
<html>
   <body>

      <h1>Hello beavis!</h1>

   </body>
</html>
# curl http://127.0.0.1:5000/hello/butthead
<!doctype html>
<html>
   <body>

      <h1>Hello butthead!</h1>

   </body>
</html>
```
Notice how in the URL, I have added */hello/beavis* and that resulted in a piece of html being returned
with that variable name in it? (i.e. Hello beavis!)
