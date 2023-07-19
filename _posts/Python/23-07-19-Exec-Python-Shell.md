---
title: Executing Python in Shell
date: 2023-07-19 01:01:00 -700
categories: [Python]
tags: [python]
---

## Executing Python in Shell
To execute Python in Shell simply use ```python3 -c```. For example, the following checks the location of your Python executable.
```
python3 -c 'import sys; print(sys.executable);'
```