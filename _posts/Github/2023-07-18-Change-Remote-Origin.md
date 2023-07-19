---
title: Change Remote Origin
date: 2023-07-18 03:00:00 -700
categories: [Github]
tags: [git,github]
---

## Change Remote Origin
Git remote set-url allows you to change the origin if you need to set a new origin.

1. View existing remote origin.
```
git remote -v
```

2. Update the remote origin.
```
git remote set-url origin git@github.com:ArcticTechnology/sandbox_updated.git
```

3. Note: If you have multiple repositories with multiple SSH keys, remember to identify which key you are using. For instance, if your key is ```github.com-personal``` then you should set your remote origin to:
```
git remote set-url origin git@github.com-personal:ArcticTechnology/sandbox_updated.git
```