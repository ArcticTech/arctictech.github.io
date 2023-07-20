---
title: Github Basics Tutorial
date: 2023-07-18 00:00:00 -700
categories: [Github]
tags: [git,github,ssh,tutorial]
---

## Github Basics Tutorial
This is a basics tutorial that will go over how to set up Github locally so you can push/pull with your SSH key.

### Objective
Once set up, you should be able to directly add/commit and push changes to your repo using the following code.
```
git add .
git commit -m "my-second-commit"
git push
```

### Prerequisite
Make sure you have git installed:
```
https://git-scm.com/
```

### Setup SSH Key
In order this up locally, you will need the local SSH key associated with your account. If you haven't set one up yet then do the following. See this guide on [using ssh with Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for details.

1. Run ssh-keygen, to create your key in ```~/.ssh/id_ed25519```.
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```
2. Next run ssh eval:
```
eval "$(ssh-agent -s)"
```
3. (Mac only) For mac users you will need to do this extra step. Skip if you are not on mac.
```
touch ~/.ssh/config
nano ~/.ssh/config
```
Then copy the following to the ~/.ssh/config file.
```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
``` 
4. Run ssh-add.
For Mac include --apple-use-keychain:
```
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
For Linux and Windows, simply:
```
ssh-add ~/.ssh/id_ed25519
```

5. Now copy the contents of the ```~/.ssh/id_ed25519.pub``` file. Should look something like this:
```
ssh-ed25519 AFSJOIAUWEREIJRIJ...your_email@example
```

6. Go to your Github account under https://github.com/settings/keys > SSH Keys, click "New SSH Key". Paste in the key you just copied. Then give it a title (usually the name of your computer that holds the key).

7. Use the following command to test that you have access.
```
ssh -T git@github.com
```
* The result should say:
```
Hi ArcticTechnology! You've successfully authenticated, but GitHub does not provide shell access.
```

### Setup Globals

This part is optional, but it allows you to default your username and email:
```
git config --global user.name "ArcticTechnology"
git config --global user.email 13512073+ArcticTechnology@users.noreply.github.com
```
Note: If you are using email privacy restrictions (which is highly recommended) you need to use this private email which Github provides: ```{ID}+{username}@users.noreply.github.com```. See this post on [email privacy](https://stackoverflow.com/questions/43378060/meaning-of-the-github-message-push-declined-due-to-email-privacy-restrictions) for details.

### Pull Your Existing Github Repo Locally
The following are instructions to pull an existing Github Repo locally.
1. Create a new repository locally: 
```
git init
```
2. Add origin:
```
git remote add origin git@github.com:ArcticTechnology/sandbox.git
```
3. Pull the existing repo:
```
git pull origin main
```
4. Rename your branch main from master as Github now defaults to main.
```
git branch -M main
```
5. Push changes and set upstream main
```
git push -u origin main
```
Once you successfully set upstream main. You should be all ready to make your commits.

### Push Up a Brand New Repo
The following are instructions to push up a new repo.
1. Create a new repository locally: 
```
git init
```
2. Add origin:
```
git remote add origin git@github.com:ArcticTechnology/sandbox.git
```
3. Rename your branch main from master as Github now defaults to main.
```
git branch -M main
```
4. Make your first commit.
```
git add .
git commit -m "first commit"
```
5. Push changes and set upstream main
```
git push --set-upstream origin main
```
Once you successfully set upstream main. You should be all ready to make your commits.

### Changing the Name of the Repo
When you change the name of your repo, be sure to update the remote origin with the following:
1. View existing remote origin.
```
git remote -v
```

2. Update the remote origin.
```
git remote set-url origin git@github.com:ArcticTechnology/sandbox_updated.git
```
Note: If you have multiple repositories with multiple SSH keys, remember to identify which key you are using. For instance, if your key is ```github.com-personal``` then you should set your remote origin to:
```
git remote set-url origin git@github.com-personal:ArcticTechnology/sandbox_updated.git
```

### Conclusion
Now your Github repo is set up. You can use the following to commit new changes:
```
git add .
git commit -m "my commit message"
git push
```
