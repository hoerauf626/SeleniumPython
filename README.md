# SeleniumPython
#Prerequisites to get started with Selenium and NodeJs
Here are the pre-quisites for getting started with Selenium and NodeJs:

Machine with node setup with npm installed
selenium-webdriver package for using it to run Selenium configurations
Chrome driver package – web browser to run the test case. This is only applicable when tests are performed on a local Selenium Grid.
Mocha assertion library
#Setting up node and npm
Note : Incase you already have node and npm installed on your system, just update them to latest version using following

1: npm install npm@latest -g

In order to install node/npm and then verify the setup follow these steps

#Download and install node just like any other program on your system from this website : nodejs.org
Once the installation completes, type following commands on your terminal window to verify it

2: node -v
3: npm -v

Now that we have installed node and verified it, let’s create a npm project directory which we will be using to add automation tests. For this follow these simple steps

#Create a new directory in your system either through the UI or by using this command on terminal
4: mkdir selenium-node-automation-project

#To make this directory as an npm project directory, navigate to it and initialize node
5: cd selenium-node-automation-project
6: npm init

Note: Running init command would throw a bunch of questions at you regarding the setup information. For starters, keep everything as default and submit.

Once all information is gathered by system, it will generate a package.json file for you in the directory. This is a config file that we can customize as required as we proceed with developing our automation.

Here’s a snapshot of how it will look like initially :

{
  "name": "selenium-node-automation-project",
  "version": "1.0.0",
  "description": "Test for npm projects",
  "main": "index.js",
  "scripts": {
    "test": "test"
  },
  "author": "Lambdatest"
}
1
2
3
4
5
6
7
8
9
10
{
  "name": "selenium-node-automation-project",
  "version": "1.0.0",
  "description": "Test for npm projects",
  "main": "index.js",
  "scripts": {
    "test": "test"
  },
  "author": "Lambdatest"
}
Configuring Selenium with Node
Once we are done with setting up node(s), next would be to install a framework to work with Selenium and node together. For this navigate to your project folder, selenium-node-automation-project and execute following command

npm install selenium-webdriver
7: npm install selenium-webdriver

Once this is installed, we download drivers for the WebDriver to interact with the specific browser under test. In this tutorial we will be downloading drivers for Firefox and Chrome as they are mostly used and can function with mostly all major operating systems.

You can download the latest GeckoDriver (for Firefox) from here and Chromedriver (for Google Chrome) from here. Next unzip them into some location/directory which is easily accessible and copy the absolute path for both the drivers and add it to your system’s PATH variables.

Having configured node and Selenium for Selenium NodeJs example, let us try to run a simple program to verify the setup. For this create a file test_setup.js inside the project folder, and add this code to it.

var webdriver = require('selenium-webdriver');
 
var driver = new webdriver.Builder().
   withCapabilities(webdriver.Capabilities.chrome()).
   build();
 
driver.get('http://www.lambdatest.com');
driver.quit();
1
2
3
4
5
6
7
8
var webdriver = require('selenium-webdriver');
 
var driver = new webdriver.Builder().
   withCapabilities(webdriver.Capabilities.chrome()).
   build();
 
driver.get('http://www.lambdatest.com');
driver.quit();
And execute it with following command


8: node test_setup.js

You should see the Chrome browser getting instantiated and redirecting to Google.
