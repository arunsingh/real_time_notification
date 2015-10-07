#RTN

Real Time Notification

Django App Real time Notification

Real Time Notification P2P tool

Real Time Notification is a peer to peer push publish subscribe notification system which will disseminate the information about moving hubs to peer delivery manpower/systems. This project adds integration tool for Django based web platforms, thus enabling you to easily push real-time notifications to your existing web applications.

In addition, it provides utilities to:

1.	Generate publish subscribe (pub/sub) driven message flow.
2.	Can send single or multiple Real time notifications.
Installation Environments and Dependencies
1.	Node.js
2.	Redis
3.	npm
4.	django 1.8.5 framework
5.	virtualenv
6.	node modules
7.	front end package managers[npm/bower]


Run the Server(s) [Assuming Unix environment]

1.	NodeJS : node node_modules/ishout.js/server.js
2.	Redis: redis-server
3.	Django-Admin

Workflow


The problem statement in question aims to build real time notification, I have developed build using publish subscribe (pub/sub) view model.  When your web app calls push server, it does so over an internal HTTP API. On the client side, your client is also connected to the nodejs server, socket.io. and redis. So when you, inside your app, send a request (let say, send a message "Hello Alok!" to user A) the django server publish API which takes that request and finds the appropriate socket(s) for a client called "A", and emits that message. Hence that is the basic workflow.

Configuration

For product build over local development server, We don’t need any settings configurations, default settings work for local environment. For production quality build over production server configuring announce is done by providing a JSON configuration file as a command line argument. 

To specify the path to this file, use the --config command line option, like so:
$ node server.js --config=/path/to/settings.json



Authorization


The real time notification authorization model works like this:
1.	Client makes a request to the iOS/Android PhoneApp/webapp.
2.	In turn webapp turns to push server internal API and requests a token for that user's ID.
3.	Once token is recieved, the webapp sets a cookie called emit Token to the value of the token, and renders the requested page back to client.
4.	The requested page (containing the server side javascript include) uses this cookie to retrieve the token, and validates it against the push server APIs.
5.	On successful validation, a connection is established and your client will start listening on channels and events you define.
6.	These steps are all handled by real time internal API  framework's which uses  iShout.js client. you just need to install ishout, include the javascript client on your page, and start the iShout.js server.
7.	AngularJS API can be integrated for more interactive frontend  alongside NodeJS back end APIs.

