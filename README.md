# ![sequal-favicon](./app/pages/favicon.png) squeal 

A smaller grunt for the Raspberry-Pi.

## Inspiration
[gruntjs.com](https://gruntjs.com/)  is big and can be unwieldy, it encourages normalization of code - which in a normal coding environment is encouraged. 
However, this makes for slow load times for pages due to network latency and running on my R-Pi this can be a pain.
This web framework de-normalises (i.e. dulicates) code css and html to achieve much faster load times. 

# Installation to Up-and-running
## Requirements
You must have installed the following on your system:
 * python (https://wiki.python.org/moin/BeginnersGuide/Download)
 * pip (https://pip.pypa.io/en/stable/installing/)

Go to the location you want to work in, on my system this is `~/dev` and pull out the code with and change to that folder with:

```
git clone git@github.com:diversemix/squeal.git
cd squeal
```

Next configure the enviroment and build the stock test pages with:

```
./configure
. env/bin/activate
./build
```
> ### Note
> * After you edit the pages don't forget to run build again to see the changes.
> * Whenever you want to build your pages make sure the virtualenv is activated.

Now you should be then able to change to the `app` folder and run the application 
with:
```
cd app
python app.py
```

Browsing to http://localhost:5000 you will see the result of the compiled pages.

# Tutorial : Hello World
Before we dive into the tutorial - let's first take a look at the folder structure:

| Folder | Description |
|--|--|
| *content* | This will contain all your content to compile. |
|*app* | This folder contains the app.py file that will run the website. It is based on a [Flask](http://flask.pocoo.org/) application to keep things simple.|
| *app/pages* | This is the compiled html files. Note, these are html files but without the extension. They will also contain the CSS embeded in there to reduce network latency of ity-bity files.|

# Containerization

On the R-Pi pull down the following Docker container (from the root folder): 
```
git clone https://github.com/jazzdd86/alpine-flask.git
```

Personally I use [docker-compose](https://docs.docker.com/compose/install/) to control the container. If you wish to do this then create a `docker-compose.yml` file such as:

```
version: '2'

services:
    webserver:
        restart: always
        build: ./alpine-flask
        volumes:
            - ./app:/app
        ports:
            - "80:80"
        environment:
            - DEBUG=1
```

Then you can start/stop the application form within the container:

```
docker-compose up
docker-compose down
```
---
Have Fun!