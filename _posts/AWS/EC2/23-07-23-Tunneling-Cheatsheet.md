---
title: Tunneling Cheatsheet
date: 2023-07-23 00:01:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,cheatsheet]
---

### Tunneling Cheatsheet

* Example 1:
```
ssh ec2-user@ec2-XX-XXX-XX-XXX.compute-1.amazonaws.com -i /user/home/mykeys/ec2key-us-east-1.pem \
  -L5901:localhost:5901 -nNT
```
* Example 2:
```
ec2-user@XX.XXX.XXX.XX -i /user/home/mykeys/ec2key-us-east-1.pem \
  -L5901:localhost:5901 -nNT
```

* Example 3:
```
ssh -L 5901:localhost:5901 -i /user/home/mykeys/ec2key-us-east-1.pem ssh ec2-user@ec2-XX-XXX-XX-XXX.compute-1.amazonaws.com
```

* Example 4:
```
ssh -L 5901:localhost:5901 -i /user/home/mykeys/ec2key-us-east-1.pem ec2-user@XX.XXX.XXX.XX
```

* Tunneling Redshift:
```
ssh ec2-user@XX.XXX.XXX.XX.us-east1.amazonaws.com -i /user/home/mykeys/ec2key-us-east-1.pem \
  -L5439:cluster.cmj39df3f.us-east-1.redshift.amazonaws.com:5439 -nNT
```