---
title: Python Virtual Environments
date: 2023-07-19 01:02:00 -700
categories: [Python]
tags: [python]
---

## Python Virtual Environments
When working on different projects in the same environment, you will likely run into conflicts among your dependencies. The best way to avoid this is to use separate virtual environments for your projects. This way any dependencies that your project or package relies on will be isolated within its own dedicated environment. To create a virtual environment use the following:

1. Create an environment:
```
python3 -m venv env1
```

2. Activate the environment:
```
source env1/bin/activate
```
* With your virtual environment, you can now install and test different packages.
Notice that you have a clean slate with the minimal packages installed:
```
pip list
```

3. To Deactivate the environment
```
deactivate
```

### Troubleshooting
If you changed the path to your venv folder (such as changing the parent folder) you might find that your command line will not use the correct python path even after activating the environment. Simply just recreate the environment, will fix the issue. See this post: https://stackoverflow.com/a/58424933