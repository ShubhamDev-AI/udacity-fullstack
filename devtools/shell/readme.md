# Shell


## Resources

 - [The Bash Academy](http://www.bash.academy/)
 - [Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
 - [BASH Programming](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
 - [RegExr](https://regexr.com/)


## Globals

```sh

$PS1        # shell prompt

$COLUMNS    # number of columns in shell window
$ROWS       # number of rows in shell window

$PWD        # working directory
$PATH       # list of executable folders

$LOGNAME    # current username
```

```sh
PATH=$PATH:/another/directory   # add directory to path
```

## Special Paths

```sh
.       # current directory
..      # parent directory
~       # home directory

```

## Common Commands


```sh

cd      # change directory

pwd     # print working directory

ls          # list current directory
ls /path
ls -l       # long list
ls *.ext    # filter by wildcard


mkdir dir_name      # make directory

mv /from /to        # move files
mv *.ext  /to       # filter by wildcard

cat                 # catenate -> concatenate
cat dictionary.txt  # echo file contents

rm file.txt         # remove file
rmdir /pasth        # remove directory
```

#### alias

```
alias               # view aliases
alias ll='ls -la'   # add alias

```


#### curl

```sh
curl                      # see URL
curl 'http://google.com'  # echo response
curl -L 'http://g.com'    # follow redirects

# output result to file / download
curl -o -L 'google.html' 'http://google.com'


```


#### less

```sh
# view interactive text file, paged
less dictionary.txt
```

 - `space` and `b` to page
 - *arrows* to scroll
 - `/` to search
 - `q` to quit


#### grep
```sh

# print things matching pattern (regex)
grep

# find 'word' in file
grep word dictionary.txt

# show less results
grep word dictionary.txt | less


```

## Command Structures

```sh
echo 'Hello world' # encapsulate string arguments
ls  'Documents/'*      # treated as wildcard
ls  'Documents/*'      # treated as actual * char
```


 - [.bashrc PS1 generator](http://bashrcgenerator.com/)


## Customization

 - Login shells on startup run `~/.bash_profile`
 - Non-login shells on startup run `~/.bashrc`

`.bash_profile` example:

```sh

# add bin folder to path
PATH=$PATH:/Users/user/bin

# source bashrc for consistency
if [-f ~/.bashrc] ; then
    source ~/.bashrc
fi

# aliases
alias ll='ls -la'
alias ..='cd ..'
alias ...='cd ...'
alias now='date + "%T"'
alias sl
```

