Docker
======

.. TODO:: @jfryman Add a DEPRECATED node here

.. warning::
   st2express is deprecated. Use on your risk. A new and better Docker and instructions are coming soon.

st2express repository contains a Dockerfile which allows you to easily and
quickly run all the |st2| components inside a single docker container.

All the services are running inside a single docker container which means
this method is great for testing and developing |st2|, but not appropriate
for production where "one service per container" model should be followed.

::

    git clone https://github.com/StackStorm/st2express.git
    cd st2express/docker/
    docker build -t st2 .

This will install all |st2| components with Mistral workflow engine on Ubuntu
14.04 docker base image. There'll be some red output, don't worry about it.
While waiting, check out |st2| :doc:`/video` for quick intro. Then run a docker
container with the st2 image that just got built

::

    docker run -it st2

Run ``/root/st2/start.sh`` inside the container to start all services including
st2.

For more information, please refer to the `README <https://github.com/StackStorm/st2express/tree/master/docker>`_
inside the st2express repository.

Distributed Containers
**********************

Each of the components are available via the Docker Hub. Take a look at https://registry.hub.docker.com/repos/stackstorm/

Fetch the following images:

::

    docker pull stackstorm/st2actionrunner
    docker pull stackstorm/st2rulesengine
    docker pull stackstorm/st2resultstracker
    docker pull stackstorm/st2notifier
    docker pull stackstorm/st2auth
    docker pull stackstorm/st2api

Each of the containers will need to be configured to connect to a MongoDB and RabbitMQ instance. Set the following
variables for each container instance:

::

    ## File Mounts:

    - /opt/stackstorm/packs - Mount a directory of all StackStorm packs exposed to the runner
    - /home/stanley/.ssh/st2_stanley_key - SSH private key to access remote systems

    ## Environment Variables
    ### SSL
    REQUESTS_CA_BUNDLE - path to trusted root CA bundles. Default: OS default

    ### StackStorm Variables
    * ST2_API_URL - URL and port to the StackStorm API Endpoint. Default: http://localhost:9101

    ### RabbitMQ Config Settings

    * ST2_RMQ_HOST - RabbitMQ hostname. Default: localhost
    * ST2_RMQ_PORT - RabbitMQ port. Default: 5672
    * ST2_RMQ_USERNAME - RabbitMQ username. Default: guest
    * ST2_RMQ_PASSWORD - RabbitMQ password. Default: guest
    * ST2_RMQ_VHOST - RabbitMQ vhost. Default: (unset)

    ### MongoDB Config Settings

    * ST2_DB_HOST - MongoDB host: Default: localhost
    * ST2_DB_PORT - MongoDB port. Default: 27017
    * ST2_DB_NAME - MongoDB database name. Default: st2
    * _ST2_DB_USERNAME_ - MongoDB username.
    * _ST2_DB_PASSWORD_ - MongoDB password.

    * Note: Italic settings are optional

The API and Auth containers will need ports exposed. Note the API container info for configuration for the rest of
the containers in your installation. Best to use service discovery to set this value. Components of StackStorm and
the st2client will use this configuration.

::

    API - TCP 9101
    Auth - TCP 9100

Startup the containers with the command ``/usr/local/bin/tiller``. For example:

::

    docker run -d -i -t stackstorm/st2sensorcontainer /usr/local/bin/tiller

Once done, see the http://docs.stackstorm.com/cli.html to configure your client to connect to API containers

Note
****

With containers, supervisord_ is often used to manage processes within the container.  Since some Stackstorm components require PATH to be properly set, pay attention to appending path the right way in supervisord configuration files: use %(ENV_PATH)s instead of $PATH.

::

    [program:st2actionrunner]
    command=python /opt/stackstorm/src/st2/st2actions/bin/st2actionrunner --config-file /etc/st2/st2.conf
    environment=PATH="/opt/stackstorm/src/st2/st2/virtualenv/bin:%(ENV_PATH)s",PYTHONPATH="/opt/stackstorm/src/st2/virtualenv/lib/python2.7/site-packages:/opt/stackstorm/src/st2/st2common:/opt/stackstorm/src/st2/st2reactor:/opt/stackstorm/src/st2/st2actions:/opt/stackstorm/src/st2/st2api:/opt/stackstorm/src/st2/st2auth"

.. _supervisord: http://supervisord.org/

.. include:: on_complete.rst
