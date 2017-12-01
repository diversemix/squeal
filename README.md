# ![sequal-favicon](./app/pages/favicon.png) squeal 

A smaller grunt for the Raspberry-Pi.

Grunt is big and can be unwieldy, it encourages normalization of code - which in a normal coding environment is encouraged. 
However, this makes for slow load times for pages due to network latency and running on my R-Pi this can be a pain.
This web framework de-normalises (i.e. dulicates) code css and html to achieve much faster load times. 

# Installation to Up-and-running

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

After you configure your environment after you edit the pages don't forget to 
run build again to see the changes.

Now you should be then able to change to the `app` folder and run the application 
with:
```
cd app
python app.py
```

Then you can browse to http://localhost:5000 and see the result.

# Pages

# Containerization

---
Have Fun!