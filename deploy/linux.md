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
 - `apt-get update` - Update package source list
 - `apt-get upgrade` - Upgrade (update) installed packages
 - `apt-get autoremove` - Remove unused packages
 - `apt-get install {package_name}` - Install package

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

*A user or account of a system is uniquely identified by a numerical number called the UID (unique identification number). There are two types of users – the root or super user and normal users. A root or super user can access all the files, while the normal user has limited access to files. A super user can add, delete and modify a user account. The full account information is stored in the `/etc/passwd` file and a hash password is stored in the file `/etc/shadow`. Some operations on a user account are discussed below.* - [Linux System Administration](https://opensourceforu.com/2017/02/linuxsusadmin/)

 - `useradd {user}` - Create a new user or update default new user information [[man]](https://linux.die.net/man/8/useradd)
   - `useradd -c “Anirban Choudhury” anirban` - Specifying a user’s full name when creating a user
   - `useradd -u 1036 anirban` - Creating a user with the UID
   - `useradd –d /home/test anirban` - Creating a user with non-default home directory
   - `useradd -g "head" -G "faculty" anirban` - Adding a user to a primary group and supplementary group
 - `passwd {user}` - Changes passwords for user accounts [[man]](http://man7.org/linux/man-pages/man1/passwd.1.html)
   - `passwd -e anirban` - Expire a user's password
   - `passwd -l anirban` - Locking a user
   - `passwd -u anirban` - Unlock a user
 - `usermod {user}` - Modifies system account files [[man]](https://linux.die.net/man/8/usermod)
   - `usermod -l “nishant” anirban` - Changing a user name
 - `userdel {user}` - Delete a user account and related files [[man]](https://www.systutorials.com/docs/linux/man/8-userdel/)
   - `userdel -r nishant` - Removing a user. -r: Files in the user's home directory will be removed along with the home directory itself and the user's mail spool.

### Groups

*Linux group is a mechanism to organise a collection of users. Like the user ID, each group is also associated with a unique ID called the GID (group ID). There are two types of groups – a primary group and a supplementary group. Each user is a member of a primary group and of zero or ‘more than zero’ supplementary groups. The group information is stored in /etc/group and the respective passwords are stored in the /etc/gshadow file.*

 - `groupadd {group}` - Creates a new group [[man]](https://linux.die.net/man/8/groupadd)
   - `groupadd employee` - Creating a group with default settings
   - `groupadd -g 1200 manager` - Creating a group with a specified GID
 - `gpasswd {group}` - Administer /etc/group, and /etc/gshadow [[man]](https://linux.die.net/man/1/gpasswd)
   - `gpasswd -r employee` - Removing group password
 - `groupmod {group}` - modifies the definition of the specified group [[man]](https://linux.die.net/man/8/groupmod)
   - `groupmod -n hrmanager employee` - Changing the group’s name
   - `groupmod -g 1050 manager` - Changing the group’s GID
 - `groupdel {group}` - Deleting a group [[man]](https://www.systutorials.com/docs/linux/man/8-groupdel/)
   - `groupdel employee` - Deleting a group

### Sudoers

*sudo (/ˈsuːduː/ or /ˈsuːdoʊ/) is a program for Unix-like computer operating systems that allows users to run programs with the security privileges of another user, by default the superuser. It originally stood for "superuser do" as the older versions of sudo were designed to run commands only as the superuser.* - [sudo - Wiki]()

Make User a sudoer:
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

Path permission descriptor format `*OOOGGGEEE` where:

 - `*` - `d` indicates the path is a directory, `-` indicates file
 - `OOO` - 3 chars indicating **owner** permissions
 - `GGG` - 3 chars indicating **group** permissions
 - `EEE` - 3 chars indicating **everyone**-else permissions

### Commands:

 - `chown {user}:{group} {file}` - Changes the user and/or group ownership of each given file [[man]](https://linux.die.net/man/1/chown)
 - `chmod {permissions} {file}` - Changes the file mode bits of each given file [[mod]](https://linux.die.net/man/1/chmod)
   - Absolute Mode: `chmod {nnn} {file}`
     - `nnn` Specifies the octal values that represent the permissions for the file owner, file group, and others, in that order.
     - Eg. `chmod 755 public_dir`
   - Symbolic Mode: `chmod who operator permission filename`
     - `who` specifies whose permissions are changed
     - `operator` specifies the operation to perform
     - `permission` specifies what permissions are changed
     - Eg. `chmod a+rx fileb`
 - `chgrp {group} {file}` - Change the group of each file to group
   - `chgrp employee somefile.txt`

### Absolute Mode (Octal)

| Octal Value | File Permissions Set | Permissions Description |
| ----------- | -------------------- | ----------------------- |
| 0           | ---                  | No permissions |
| 1           | --x                  | Execute permission only |
| 2           | -w-                  | Write permission only |
| 3           | -wx                  | Write and execute permissions |
| 4           | r--                  | Read permission only |
| 5           | r-x                  | Read and execute permissions |
| 6           | rw-                  | Read and write permissions |
| 7           | rwx                  | Read, write, and execute permissions |

### Symbolic Mode

| Symbol | Function   | Description |
| ------ | ---------- | ----------- |
| u      | Who        | User (owner) |
| g      | Who        | Group |
| o      | Who        | Others |
| a      | Who        | All |
| =      | Operation  | Assign |
| +      | Operation  | Add |
| -      | Operation  | Remove |
| r      | Permission | Read |
| w      | Permission | Write |
| x      | Permission | Execute |
| l      | Permission | Mandatory locking, setgid bit is on, group execution bit is off |
| s      | Permission | setuid or setgid bit is on |
| S      | Permission | suid bit is on, user execution bit is off |
| t      | Permission | Sticky bit is on, execution bit for others is on |
| T      | Permission | Sticky bit is on, execution bit for others is off |

## Ports