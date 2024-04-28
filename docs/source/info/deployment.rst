Deployment
==========


.. figure:: /images/information/deploymentDiagram.png
   :alt: deployment diagram
   :align: right

The end-user interacts with our application through any web browser that supports javascript.
The browser component serves as the user interface or client-side of the application, running directly on the user's device.

The browser communicates with our `server <https://sysrev.cs.binghamton.edu>`_ that is running a Nginx Engine,
which acts as the web server and reverse proxy server for the application.
Nginx is an open-source software known for its high performance, stability, and ability to handle a large number of concurrent connections.
It is responsible for load balancing, caching, and serving static content for the application.
The Nginx Engine, in turn, interacts with two main components: SysReview and Argus.

Based on the provided route, nginx proxies the request to the corresponding application.
In summary, the end-user accesses the application through a web browser, which communicates with the Nginx Engine that
handles web server and proxy tasks. The Nginx Engine then routes requests or delegates tasks to the SysReview and Argus
components, which handle system monitoring and security/monitoring functions, respectively.

This deployment architecture aims to provide a scalable, secure, and efficient way to deliver features and
functionalities of both the application to the end-users.
