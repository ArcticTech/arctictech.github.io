---
title: Git Rebase
date: 2023-07-18 04:00:00 -700
categories: [Github]
tags: [git,github]
---

## Git Rebase
If you have ever found yourself in a situation where you made a bunch of commits in your code, but you would only like to push all of those changes up as one single commit. This situation is very typical in development, and the way you can do this is to use Git Rebase. It allows you to reapply commits on top of another base tip. To use Git Rebase, do the following:

1. Say you already have a commit and you want to add and commit another change.
```
git add .
git commit -m "want to fixup this change"
```

2. Next, use ```git rebase -i```
```
git rebase -i
```

3. In the interactive window pick the commit you want and make the others fixup and save changes.

4. Push the changes.
```
git push
```