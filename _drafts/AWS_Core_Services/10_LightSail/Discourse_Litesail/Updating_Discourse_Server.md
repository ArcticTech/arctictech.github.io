## Updating Discourse Guide
If you self-host Discourse, you occasionally need to run a manual update via the command line to get the latest security releases newest libraries. These updates are not picked up in admin/upgrade, which is why you’ll occasionally need to do this additional step.

### Steps to Update Discourse

1. SSH into the instance and run update + upgrade the instance.
```
sudo apt update
sudo apt-get dist-upgrade
sudo apt full-upgrade
```
* Note: It's a good idea to have automatic security updates enabled for your server if you have not done so already:
```
dpkg-reconfigure -plow unattended-upgrades
```

2. Discourse itself should be updated about twice a month, by clicking the “Update to Latest Version” button in your admin dashboard ( admin/upgrade). We do beta releases roughly once every week.

3. Every two months, SSH into your web server.
```
cd /var/discourse
sudo git pull
sudo ./launcher rebuild app
```

Due to the way docker packaging has changed you may also have to update your docker from lxc-docker or docker-engine packages. One way to do that is via the Docker script here (it will warn about an existing install but should upgrade ok):
```
wget -qO- https://get.docker.com/ | sh
```
This will now use the docker-ce main versions.

This is completely safe, we have never seen anything get broken by base Ubuntu updates.

To summarize:
* update Discourse twice a month via web updater
* update the container every two months
* update the OS every six months

You could double these numbers and still be fairly safe, e.g. update Discourse once a month, container every 4 months, OS once every 12 months, and so on.

But you really, really want automatic security updates enabled in Ubuntu, as listed above.

### FAQ

#### What is the right time to update?
It just depends on the time you have available and how close to bleeding edge you want to be. If you have non-official plugins, it is highly advisable to utilize a test/staging site. If you do not have any non-official plugins, you can likely upgrade immediately, but even then, some plugins may break for a couple of days as the team fixes them (there are a lot of them).

#### What is common practice when updating with many plugins installed?
If you have a lot of plugins, testing locally or on a test server is highly advised. Especially if you have non-official plugins, as something could have broken. If you find something does break, then it is a matter of, do you have time to fix it? Does the original plugin author have time to fix it? Either of those could take weeks. So at least this way, you simply have a broken test site and not a broken production site.

#### I’m running low on disk space
If you are running low on disk space (check with df) try clearing up old images using:
```
./launcher cleanup
apt-get autoclean
apt-get autoremove
```

#### Does updating the actual server version of Ubuntu matter since Discourse always operates in Docker?
It matters a lot less. But you should be on at least Ubuntu 18.04 LTS, which will reach its end of support life 47 in April 2023. All previous versions have already reached their end of life.


