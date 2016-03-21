Title: Installing and Running Shiny Server from Source on 32-bit Ubuntu
Date: 2016-03-20 20:00
Authors: Michael Toth
Modified: 2016-03-20 20:00
Category: R
Tags: R, Projects, Shiny
Slug: installing-and-running-shiny-server-from-source-on-32-bit-ubuntu
author_gplusid: 103836786232018210272
Summary: Include Summary

My sources:
Installation: https://www.rstudio.com/products/shiny/download-server/
Digital Ocean Tutorial (Maybe don't need): https://www.digitalocean.com/community/tutorials/how-to-set-up-shiny-server-on-ubuntu-14-04
Building from Source: https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-Source
Blog for Digital Ocean Setup: http://deanattali.com/2015/05/09/setup-rstudio-shiny-server-digital-ocean/
Example Shiny App for Initial Deploy: http://shiny.rstudio.com/tutorial/lesson1/

# Installation
Assuming you don't have R installed, you'll need to do that. We'll need r-base and r-devel both installed for some shiny apps to run properly, so let's do that:

```bash
sudo apt-get update
sudo apt-get install r-base r-base-dev
```

Next we'll install the shiny R package.  While we could start up an R session and simply run install.packages('shiny') from that instance, that would install the shiny package only for one user.  Instead, we'll run the command below which will install the shiny package for all users on the machine:

```bash
sudo su - -c "R -e \"install.packages('shiny', repos='http://cran.rstudio.com/')\""
```

It's possible you may run into some dependency issues with the above command or some of those further below, in which case you should make sure you have all of the necessary software on your system installed.  The following software is all needed (sudo apt-get install any of the below that are missing)
* python 2.6 or 2.7
* cmake >= 2.8.10
* gcc
* g++
* git

RStudio provides a convenient .deb install with pre-compiled binaries for 64-bit architecture, but if you're running 32-bit architecture you'll need to build from source as described below.  If you do have 64-bit architecture you can follow the simpler instructions from RStudio to install (https://www.rstudio.com/products/shiny/download-server/)

cd into the directory where you'd like the shiny-server repository. I'll be installing mine to ~/dev, but any location will work

```bash
cd ~/dev

# Clone the repository from GitHub
git clone https://github.com/rstudio/shiny-server.git

cd shiny-server

# Add the bin directory to the path so we can reference node
DIR=`pwd`
PATH=$DIR/bin:$PATH

PYTHON=`which python`

# Check the version of Python. If it's not 2.6.x or 2.7.x, you'll need to change the "which python" above to reference the correct python installation (e.g. which python26).  For more details, check the "Python" section of the RStudio documentation here: https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-Source
$PYTHON --version

# Use cmake to prepare the make step. Modify the "--DCMAKE_INSTALL_PREFIX"
# if you wish the install the software at a different location.
mkdir tmp; cd tmp
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DPYTHON="$PYTHON" ../

# Recompile the npm modules included in the project
make
mkdir ../build
(cd .. && ./bin/npm --python="$PYTHON" rebuild)
# Need to rebuild our gyp bindings since 'npm rebuild' won't run gyp for us.
(cd .. && ./bin/node ./ext/node/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js --python="$PYTHON" rebuild)

# Install the software at the predefined location
sudo make install
```

Now we've successfully installed Shiny Server in the location we defined above (/usr/local unless you changed the DCMAKE_INSTALL_PREFIX variable).  You can now safely delete the shiny-server git repo if you would like. There are a few configuration issues we need to finalize before we can use shiny-server, which we'll cover next.

```bash
# Place a shortcut to the shiny-server executable in /usr/bin. As /usr/bin should already be in your PATH variable, you won't need to permanently modify your PATH to reflect the change we made above
sudo ln -s /usr/local/shiny-server/bin/shiny-server /usr/bin/shiny-server

#Create shiny user. On some systems, you may need to specify the full path to 'useradd'
sudo useradd -r -m shiny

# Create log, config, and application directories
sudo mkdir -p /var/log/shiny-server
sudo mkdir -p /srv/shiny-server
sudo mkdir -p /var/lib/shiny-server
sudo chown shiny /var/log/shiny-server
sudo mkdir -p /etc/shiny-server
```

Shiny server will look for resources in certain file paths.  Certain log directories and application directories can be modified in a configuration file stored at /etc/shiny-server/shiny-server.conf.  By default, there will be no file at that location.  The RStudio instructions claim that the default configuration(link) will be used if no file exists, but that was not the case for me and I received an error message when trying to run.  If the same happens for you, simply copy the default configuration into /etc/shiny-server/shiny-server.conf and you should be all set.

Now we have shiny installed and configured properly.  You'll still need to set it up to serve the files to your actual website address however.  



Getting shiny server to start automatically
