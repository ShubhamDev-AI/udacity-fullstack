# Execution Examples

```
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-149-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Mon Jun 11 20:37:46 UTC 2018

  System load:  0.82              Processes:           80
  Usage of /:   3.9% of 39.34GB   Users logged in:     0
  Memory usage: 24%               IP address for eth0: 10.0.2.15
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.

New release '16.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Sat Jun  9 13:06:12 2018 from 10.0.2.2
```
```
vagrant@vagrant-ubuntu-trusty-64:~$
```

## Directories

`ls -lah /etc`

```

drwxr-xr-x  2 root root   4.0K Jun  5 20:43 cron.d
drwxr-xr-x  2 root root   4.0K Jun  5 20:46 cron.daily
drwxr-xr-x  2 root root   4.0K Jun  5 20:43 cron.hourly
drwxr-xr-x  2 root root   4.0K Jun  5 20:43 cron.monthly
drwxr-xr-x  2 root root   4.0K Jun  5 20:46 cron.weekly
-rw-r--r--  1 root root    761 Jun  9 12:48 group
-rw-r--r--  1 root root     92 Feb 20  2014 host.conf
-rw-r--r--  1 root root     25 Jun  6 18:16 hostname
-rw-r--r--  1 root root    221 Jun  5 20:41 hosts
-rw-r--r--  1 root root    411 Jun  5 20:45 hosts.allow
-rw-r--r--  1 root root    711 Jun  5 20:45 hosts.deny
-rw-r--r--  1 root root   1.5K Jun  9 12:48 passwd
drwxr-xr-x  2 root root   4.0K Jun  9 14:33 ssh
-r--r-----  1 root root    755 May 29  2017 sudoers
drwxr-x---  2 root root   4.0K Jun  9 13:23 sudoers.d
drwxr-xr-x  2 root root   4.0K Jun  5 20:44 vim
...
```


`ls -lah /var`

```
drwxr-xr-x  2 root root   4.0K Jun  7 06:34 backups
drwxr-xr-x 12 root root   4.0K Jun  7 06:33 cache
drwxr-xr-x 48 root root   4.0K Jun  7 06:33 lib
drwxrwxr-x 10 root syslog 4.0K Jun 11 20:33 log
drwxrwxrwt  2 root root   4.0K Jun  5 20:46 tmp
...
```

`ls -lah  /home/vagrant`

```
-rw-r--r--  1 root root 3.1K Feb 20  2014 .bashrc
-rw-r--r--  1 root root  140 Feb 20  2014 .profile
drwx------  2 root root 4.0K Jun  6 18:16 .ssh
```

## Apt

`cat /etc/apt/sources.list` - List Sources

```
## Note, this file is written by cloud-init on first boot of an instance
## modifications made here will not survive a re-bundle.
## if you wish to make changes you can:
## a.) add 'apt_preserve_sources_list: true' to /etc/cloud/cloud.cfg
##     or do the same in user-data
## b.) add sources in /etc/apt/sources.list.d
## c.) make changes to template file /etc/cloud/templates/sources.list.tmpl
#

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://archive.ubuntu.com/ubuntu trusty main restricted
deb-src http://archive.ubuntu.com/ubuntu trusty main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://archive.ubuntu.com/ubuntu trusty-updates main restricted
deb-src http://archive.ubuntu.com/ubuntu trusty-updates main restricted
...
```

`sudo apt-get update` - Update package source list

```
Ign http://archive.ubuntu.com trusty InRelease
Get:1 http://security.ubuntu.com trusty-security InRelease [65.9 kB]
Get:2 http://archive.ubuntu.com trusty-updates InRelease [65.9 kB]
Hit http://archive.ubuntu.com trusty-backports InRelease
Hit http://archive.ubuntu.com trusty Release.gpg
Get:3 http://security.ubuntu.com trusty-security/main Sources [156 kB]
Get:4 http://archive.ubuntu.com trusty-updates/main Sources [416 kB]
Get:5 http://security.ubuntu.com trusty-security/universe Sources [73.8 kB]
Get:6 http://archive.ubuntu.com trusty-updates/restricted Sources [6,322 B]
...
Fetched 12.5 MB in 1min 16s (163 kB/s)
Reading package lists... Done
```

`sudo apt-get upgrade` - Upgrade (update) installed packages

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

`sudo apt-get autoremove` - Remove unused packages

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

`sudo apt-get install finger` - Install package

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  finger
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/17.3 kB of archives.
After this operation, 68.6 kB of additional disk space will be used.
Selecting previously unselected package finger.
(Reading database ... 63130 files and directories currently installed.)
Preparing to unpack .../finger_0.17-15_amd64.deb ...
Unpacking finger (0.17-15) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
Setting up finger (0.17-15) ...
```

`sudo apt-get remove finger` - Remove Package

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  finger
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 68.6 kB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 63136 files and directories currently installed.)
Removing finger (0.17-15) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
```

## finger

Use `finger` to list all user's last login

```
Login     Name       Tty      Idle  Login Time   Office     Office Phone
vagrant              pts/0          Jun  9 12:31 (10.0.2.2)
```

`finger vagrant` - Display information about user 'vagrant'.

```
Login: vagrant                          Name:
Directory: /home/vagrant                Shell: /bin/bash
On since Sat Jun  9 12:31 (UTC) on pts/0 from 10.0.2.2
   2 seconds idle
No mail.
No Plan.
```

## Users

`cat /etc/passwd` - List of users with their passwords

```
root:x:0:0:root:/root:/bin/bash
vagrant:x:1000:1000::/home/vagrant:/bin/bash
ubuntu:x:1001:1001:Ubuntu:/home/ubuntu:/bin/bash
student:x:1002:1002:Student,,,:/home/student:/bin/bash
```

`cat /etc/sudoers` - List of users with sudo access

```
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```

`cat /etc/sudoers.d/vagrant`

```
# CLOUD_IMG: This file was created/modified by the Cloud Image build process
vagrant ALL=(ALL) NOPASSWD:ALL
```