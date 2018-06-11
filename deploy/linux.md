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
/home/vagrant   # user vagrant's home directory
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

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

## Apt-Get

A list of sources for installing packages/apps can be found at `/etc/apt/sources.list`.

Find Ubuntu Trusty packages at: [https://packages.ubuntu.com/trusty/](https://packages.ubuntu.com/trusty/)

 - `cat /etc/apt/sources.list` - List sources
 - `sudo apt-get update` - Update package source list
 - `sudo apt-get upgrade` - Upgrade (update) installed packages
 - `sudo apt-get autoremove` - Remove unused packages
 - `sudo apt-get install {package_name}` - Install package

### Manuals

To read the manual for a given app run `man {exe}`

```sh
man apt-get
```


## Security

### The rule of least privilege

*In information security, computer science, and other fields, the principle of least privilege (PoLP, also known as the principle of minimal privilege or the principle of least authority) requires that in a particular abstraction layer of a computing environment, every module (such as a process, a user, or a program, depending on the subject) must be able to access only the information and resources that are necessary for its legitimate purpose.* - [Wiki - Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)


 - `cat /etc/passwd` - List of users with their passwords.
   - Formatted: `{username}:{enc_password}:{user_id}:{group_id}:{description}:{home_dir}:{default_shell}`
   - Eg. `vagrant:x:1000:1000::/home/vagrant:/bin/bash`
 - `cat /etc/sudoers` - List of users with sudo access
   - Eg. `root    ALL=(ALL:ALL) ALL`
   - Do not edit this OS generated file
 - `ls /etc/sudoers.d` - Directory with additional sudo user files.
   - Eg. `/etc/sudoers.d/vagrant` with `vagrant ALL=(ALL) NOPASSWD:ALL`


### finger

The `finger` displays information about the system users.

*Finger displays the user's login name, real name, terminal nameand write status (as a ''*'' after the terminal name if writepermission is denied), idle time, login time, office location andoffice phone number.
Login time is displayed as month, day, hours and minutes, unlessmore than six months ago, in which case the year is displayedrather than the hours and minutes.
Unknown devices as well as nonexistent idle and login times aredisplayed as single asterisks.* - [finger(1) - Linux man page](https://linux.die.net/man/1/finger)

 - `finger` - Display info on all users
 - `finger {username}` - Display info on specified user

## Users

[adduser(8) - Linux man page](https://linux.die.net/man/8/adduser)

 - `sudo useradd {username}` - Create a new user or update default new user information
 - `sudo passwd -e {username}` - Expire a user's password

### Sudoers

*sudo (/ˈsuːduː/ or /ˈsuːdoʊ/) is a program for Unix-like computer operating systems that allows users to run programs with the security privileges of another user, by default the superuser. It originally stood for "superuser do" as the older versions of sudo were designed to run commands only as the superuser.* - [sudo - Wiki]()

 - Make User a sudoer:
   - Add a new file to the additional sudoers directory, `/etc/sudoers.d`:
   - Eg. Add line `student ALL=(ALL) NOPASSWD:ALL` to `/etc/sudoers.d/student`

## SSH

`ssh {username}@host -p {port} -i {private_key_path}`

#### SSH with public/private key pair

 - Generate new public/private key pair with `ssh-keygen`
 - Add the public key `ssh-rsa AAAA...` to `~/.ssh/autorized_keys`
 - Set the correct file permissions:
   - `chmod 700 .ssh`
   - `chmod 644 .ssh/authorized_keys`
 - ssh using private key:
   - `ssh student@127.0.0.1 -p 2222 -i ~/.ssh/id_rsa`

#### Force SSH login

 - Edit `/etc/ssh/sshd_config`
 - Set `PasswordAuthentication no`
 - Restart ssh `sudo service ssh restart`



## File Permissions

 - `r` = read
 - `w` = write
 - `x` = execute

Path permission descriptor `*---^^^&&&` where:
 - `*` - `d` indicates the path is a directory, `-` indicates file
 - `---` - 3 chars indicating **owner** permissions
 - `^^^` - 3 chars indicating **group** permissions
 - `&&&` - 3 chars indicating **everyone**-else permissions

