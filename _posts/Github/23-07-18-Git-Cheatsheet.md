---
title: Git Cheatsheet
date: 2023-07-18 05:00:00 -700
categories: [Github]
tags: [git,github,cheatsheet]
---

## Git Cheatsheet
This is a cheatsheet of the most commonly used Git commands.

1. Configuring Git:
```
git config --global user.name "Example"
git config --global user.email example@example.com
```

2. Initializing a repo and adding remote origin.
```
git init - innitializes empty git repo in current directory
git remote add origin git@github.com:ArcticTechnology/sandbox.git
git branch -M main
```

3. Check the status of untracked files.
```
git status
```

4. Adding files to repo and committing changes.
```
git add .
git commit -m "My Commit Message"
```

5. Push files to Github.
```
git push
```

6. Pulling files from Github
```
git pull
```

7. Forking projects from Github
```
git clone
```

8. Fixing up a commit, for combining multiple commits into one.
```
git rebase -i
```

9. Resetting a commit, if you want to redo a commit that you havent pushed yet.
```
git reset @~
```






