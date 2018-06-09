# Linux

```sh
vagrant@vagrant-ubuntu-trusty-64:~$
```

**Where**:
 - `vagrant` is the current logged in user
 - `vagrant-ubuntu-trusty-64` is the hostname of the current machine


## Important Directories

```sh
/               # root directory
/home           # user's home directories
/home/vagrant   # user 'vagrant' home directory
/etc            # configuration files
/var            # 'variable files' - changing in size over time, like log files
/bin            # executable binaries, available to all users
/lib            # libraries supporting binaries
/usr            # binaries, not required during bootup
/root           # home directory of the 'root' user
```

### Finding exe's

Linux will look through all the directories listed in `$PATH` to find an executable.
Execute `echo $PATH` to see the list of directories.

## Apps

A list of sources for installing packages/apps can be found at `/etc/apt/sources.list`.

Find Ubuntu Trusty packages at: [https://packages.ubuntu.com/trusty/](https://packages.ubuntu.com/trusty/)

### List sources:

```sh
cat /etc/apt/sources.list
```

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

### Update package source list:

```sh
sudo apt-get update
```

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

### Upgrade (update) installed packages:

```sh
sudo apt-get upgrade
```
```
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

### Remove unused packages:

```sh
sudo apt-get autoremove
```
```
Reading package lists... Done
Building dependency tree
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

### Install package:

```sh
sudo apt-get install finger
```

### Manuals

To read the manual for a given app run `man {exe}`

```sh
man apt-get
```


## Security

### The rule of least privilege

*In information security, computer science, and other fields, the principle of least privilege (PoLP, also known as the principle of minimal privilege or the principle of least authority) requires that in a particular abstraction layer of a computing environment, every module (such as a process, a user, or a program, depending on the subject) must be able to access only the information and resources that are necessary for its legitimate purpose.* - [Wiki - Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

