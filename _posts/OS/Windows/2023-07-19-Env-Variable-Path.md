---
title: Env Variable Path
date: 2023-07-19 00:01:00 -700
categories: [OS,Windows]
tags: [windows,windows-tricks]
---

## Setting up Environmental Variable Path
1. Write the following to the ```.bashrc```:
```
export PATH_TO_NODE="C:\Users\Hello\AppData\Roaming\npm;C:\'Program Files'\nodejs"
export PATH="$PATH:$PATH_TO_NODE"
```

2. Then, use the following command to see your new environment variable.
```
env|grep PATH
```
