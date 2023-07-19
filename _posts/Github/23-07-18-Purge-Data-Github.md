---
title: Purge Data from Github
date: 2023-07-18 02:00:00 -700
categories: [Github]
tags: [git,github,bfg]
---

## Purge Unwanted Data from Github
If you commit sensitive data, such as a password or SSH key into a Git repository, you can remove it from the history. The easiest way to do this is to use the BFG Repo-Cleaner open-source tool.

### Prerequisite
Install the BFG repo cleaner at: https://rtyley.github.io/bfg-repo-cleaner/.

### Purge Text with BFG
1. First, delete the text from your local repo and then commit and push so that your repo is in the desired state.
```
git add .
git commit -m "message"
git push
```

2. Create a file on your desktop called ```replace.txt``` and in this file add the specific texts that you want to replace in the following way:
```
TEXT_TO_REPLACE1==>new_text
TEXT_TO_REPLACE2==>new_text2
TEXT_TO_REPLACE2==>             # (Replace with the empty string)
```

3. Next, in your local git repo, run the following:
```
java -jar /Users/username/Local_Apps/bfg-1.14.0.jar --replace-text /Users/username/Desktop/replace.txt
```

4. Reflog and use the git gc command to strip out the unwanted dirty data, which Git will now recognize as surplus to requirements.
```
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

5. After the file is removed, you must force push your changes to GitHub. Force pushing rewrites the repository history, which removes the file from the commit history.
```
git push --force
```

### Purge a File or Folder with BFG

1. First, delete the desired files from your local repo and then commit and push so that your repo is in the desired state.
```
git add .
git commit -m "message"
git push
```
2. Delete a file or folder with the following.
* To delete files, run BFG on the file you want to purge. BFG will purge the history of commits.
```
java -jar /Users/username/Local_Apps/bfg-1.14.0.jar --delete-files 'File.txt'
```
* To delete folders, run BFG on the folder you want to purge. BFG will purge the history of commits.
```
java -jar /Users/username/Local_Apps/bfg-1.14.0.jar --delete-folders 'File'
```
3. Reflog and use the git gc command to strip out the unwanted dirty data, which Git will now recognize as surplus to requirements.
```
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```
4. After the file is removed, you must force push your changes to GitHub. Force pushing rewrites the repository history, which removes the file from the commit history.
```
git push --force
```

### Conclusion
BFG is a simple easy-to-use tool. Use it to fully purged your repo of unwanted files and data.

