---
title: Multiple Github Accounts with SSH
date: 2023-07-18 01:00:00 -700
categories: [Github]
tags: [git,github,ssh]
---

## Managing Multiple Github Accounts with SSH Keys
This guide will go over how to manage multiple SSH keys when you have multiple Github accounts.

### Setup SSH Key
In order this up locally, you will need the local SSH key associated with your account. If you haven't set one up yet then do the following. See this link for a more detailed guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

1. Run ssh-keygen for each of your accounts:
```
ssh-keygen -t ed25519 -C "account1_email@example.com"
ssh-keygen -t ed25519 -C "account2_email@example.com"
```

2. Save the keys with different names:
```
~/.ssh/id_ed25519_work
~/.ssh/id_ed25519_personal
```

3. Next run ssh eval:
```
eval "$(ssh-agent -s)"
```
4. (Mac only) For Mac users, you will need to do this extra step. Skip if you are not on Mac.
```
touch ~/.ssh/config
nano ~/.ssh/config
```
Then copy the following to the ~/.ssh/config file. In Host add a -suffix after github.com to distinguish the two keys
```
Host github.com-work
    HostName github.com
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes

Host github.com-personal
    HostName github.com
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes
``` 
5. Run ssh-add.
For Mac include --apple-use-keychain:
```
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_work
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_personal
```
For Linux and Windows, simply:
```
ssh-add ~/.ssh/id_ed25519_work
ssh-add ~/.ssh/id_ed25519_personal
```

6. Now copy the contents of each of the .pub files. Content should look something like this:
```
ssh-ed25519 AFSJOIAUWEREIJRIJ...your_email@example
```

7. Go to each of your Github accounts under https://github.com/settings/keys > SSH Keys, click "New SSH Key". Paste in the key you just copied. Then give it a title (usually the name of your computer that holds the key).

8. Use the following command to test that you have access to each account. The trick is you must add a dash to the suffix you used to name the hosts in the config file.
```
ssh -T git@github.com-work
ssh -T git@github.com-personal
```
* The result should say:
```
Hi Account1! You've successfully authenticated, but GitHub does not provide shell access.
Hi Account2! You've successfully authenticated, but GitHub does not provide shell access.
```

### Conclusion
Now you should be able to add a remote origin for the different projects that belong to each account. The trick is you must add a dash to the suffix you used to name the hosts after git@github.com to identify which key you want to use. Example:
```
git remote add origin git@github.com-personal:Account2/my_project.git
```
