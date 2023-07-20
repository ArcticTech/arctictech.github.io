---
title: Selenium EC2 Setup
date: 2023-07-19 02:01:00 -700
categories: [Selenium]
tags: [selenium,python]
---

## Selenium EC2 Setup Guide
This guide goes over how to deploy selenium on an Amazon EC2 instance. Make sure you know how to setup an EC2 instance first before attempting this guide.

### Upgrade Python and Pip
1. Check your python version.
```
python3 --version
```
2. If your python version is not the latest, do the following:
```
sudo amazon-linux-extras install python3.x
```
3. Then check the location of the installed package:
```
which python3.x
```
4. Then update python3 parameter to your newly installed version of python.
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.x 1
python3 --version
```
5. Test that your new python version is working.
```
python3 -c 'import sys; print(sys.executable);'
```
See this post for details: https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu
6. Upgrade pip.
```
pip3 install --upgrade pip
```
7. Check pip version and list packages.
```
pip3 --version
pip3 list
```

### Install Selenium and its Dependencies
Now we can install Selenium on our EC2 instance.

1. Install Selenium with pip3:
```
pip3 install selenium
python3 -c 'import selenium; print(selenium);'
```

2. Install Dependencies:
```
sudo yum install xorg-x11-server-Xvfb
sudo yum install glib2 libX11 nss
sudo yum install expat fontconfig
```

### Install the Chrome Browser and Driver
You will need to install both the Chrome browser and its associated driver. This will allow you to run Selenium in headless mode.

1. Get the Chrome browser.
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum install google-chrome-stable_current_x86_64.rpm
```

2. Install updates.
```
sudo yum update
```

3. Check the Chrome version and make a note of it.
```
google-chrome --version
```
4. Find the associated Chrome driver version:
```
https://chromedriver.storage.googleapis.com/index.html
```
5. Install the Chrome driver.
```
mkdir -p chromedriver
cd chromedriver
curl -SL https://chromedriver.storage.googleapis.com/XXX.X.XXXX.XX/chromedriver_linux64.zip > chromedriver.zip
unzip chromedriver.zip
mv chromedriver chromedriverXXX_X_X
rm chromedriver.zip
```
6. Check the version of your driver and make sure it matches the version of your Chrome.
```
./chromedriver --version
```

### Alternative: Install Headless Chrome
Instead of using a Chrome browser, you can use the Headless Chrome binary. The advantage of this is you don't need a browser. The downside of this is the headless chrome binary package is not frequently maintained. Currently, can only use it with the 86.0.4240.22 version of the Chrome driver.

1. Create a Chrome driver directory.
```
mkdir -p chromedriver
cd chromedriver
```

2. Get the headless Chrome binary.
```
curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-57/stable-headless-chromium-amazonlinux-2.zip > headless-chromium.zip
unzip headless-chromium.zip
rm headless-chromium.zip
```

3. Install the Chrome driver 86.0.4240.22 version.
```
curl -SL https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip > chromedriver.zip
unzip chromedriver.zip
rm chromedriver.zip
```

### Run Selenium
Run Selenium with the following code. Note that if you use the alternative method of the headless chrome uncomment out binary_location and options.binary_location.

```
#!/usr/bin/python3 -B
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#
driver_location = r'/home/ec2-user/chromedriver/chromedriver'
# binary_location = r'/home/ec2-user/chromedriver/headless-chromium'
#
service = Service(driver_location)
options = Options()
# options.binary_location = binary_location
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
#
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.google.com/')
driver.close()
driver.quit()
print('Selenium Initialized!')
```

### Uninstalling the Chrome Driver
To uninstall the Chrome driver use the following command:
```
sudo yum remove google-chrome
```