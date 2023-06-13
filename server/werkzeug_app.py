#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

'''
This is the sole function inside of script. 
You can call it anything, we used application 
It is decoreaated with the Request.applciation method, which tells it to run any
code inside of the function in the browser at the location we specify with our
development server.
'''
@Request.application
def application(request):
  print(f'This web server is running at {request.remote_addr}')
  return Response('A WSGI generated this response!')

'''
The run_simple() method runs a server for a one-page application w/o complications
Not suited for a production server that supports millions of users, but gives us
the tools needed to develop new pages for web apps that we eventually deploy to 
those servers
'''
if __name__ == '__main__':
  from werkzeug.serving import run_simple
  # run_simple() requires three args: hostname (usually localhost), port, application
  run_simple(
    hostname='localhost',
    port=5555,
    application=application
  )
  
  