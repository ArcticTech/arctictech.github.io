---
title: Resetting Old MacBook
date: 2023-07-18 12:00:00 -700
categories: [OS,Mac]
tags: [mac,mac-tricks]
---

## Resetting Old MacBook (2017+older)
1. On startup hold the command + s till the black terminal boots up.
2. In the terminal mount a new root with the following command:
```
mount -uw /
```
3. Remove the /var/db/.applesetupdone
```
rm /var/db/.applesetupdone
```
4. Shutdown /h now.
```
shutdown /h now
```
5. Turn back on the laptop and you should be prompted to set up your macbook.

