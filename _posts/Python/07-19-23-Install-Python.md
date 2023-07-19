---
title: Install Python on Linux
date: 2023-07-19 01:00:00 -700
categories: [Python]
tags: [python,linux]
---

## Install Python and Pip on Linux
1. Check you're python version with the following:
```
python3 --version
```
2. If your python version is not the latest, do the following:
```
sudo apt install python3.x -y
```
* Note: if you are installing on an EC2 amazon linux, then use the following.
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

6. Update pip.
```
pip3 install --upgrade pip
```
* Note: if you don't have pip3 install it:
```
sudo apt install python3-pip
```
7. Check pip version and list packages.
```
pip3 --version
pip3 list
```

### Alternative Install via Python.org

1. Download and install python directly from python.org:
```
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.x.x/Python-3.x.x.tgz
sudo tar xzvf Python-3.x.x.tgz
```
Note: if unzipping local file then use:
```
tar xvf Python-3.x.x.tar.xz
```
Then, execute configure and install:
```
cd Python-3.x.x/
./configure --with-openssl=/usr/src/openssl-1.0.2o --enable-optimizations
sudo make -j 4
sudo make altinstall
```

2. Update python3 parameter to your newly installed version of python.
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.x 1
python3 -c 'import sys; print(sys.executable);'
python3 --version
```