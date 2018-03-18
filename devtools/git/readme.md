# Git

## Resources

 - [Git Internals - Plumbing and Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
 - [Customizing Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
 - [Git Basics - Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
 - [Inspecting a repository](https://www.atlassian.com/git/tutorials/inspecting-a-repository)


## Git Flow

```
Working Directory

==>  git add  ==>
<==  git rm --cached <==

Staging Index

==> git commit ==>

Repository

```


## Configuration

```sh
# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# makes sure that Git output is colored
git config --global color.ui auto

# displays the original state in a conflict
git config --global merge.conflictstyle diff3


git config --global core.editor "code --wait"

git config --list
```

## `.git` Directory

The `.git` directory contains:

 - `config` file - where all project specific configuration settings are stored.
 - `description` file - this file is only used by the GitWeb program
 - `hooks` directory - this is where we could place client-side or server-side scripts that we can use to hook into Git's different lifecycle events
 - `info` directory - contains the global excludes file
 - `objects` directory - this directory will store all of the commits we make
 - `refs` directory - this directory holds pointers to commits (basically the "branches" and "tags")

## Commands

`git init` - Creates an empty Git repository [Docs](https://git-scm.com/docs/git-init)


`git clone` - Clone a repository into a new directory [Docs](https://git-scm.com/docs/git-clone)

`git status`- [Docs](https://git-scm.com/docs/git-status)

`git log` - Shows the commit logs. [Docs](https://git-scm.com/docs/git-log)

`git log --oneline` - Display file changes summary

`git log -p` - Display actual file changes

`git add <file>` - Move files from the Working Directory to the Staging Index (Stage)
`git add .` - Stage all files in the current directory

`git rm --cached <file>` - Move a file from the Staging Index back to the Working Directory (Unstage)

`git commit` - Commit changes to the repository
`git commit -m '<message>'` - Commit with message

`git diff` - See changes that have been made but haven't been committed [Docs](https://git-scm.com/docs/git-diff)

## Commit Messages

*The best way that I've found to come up with a commit message is to finish this phrase, "This commit will...". However, you finish that phrase, use that as your commit message.*


*When you're writing the commit message, the first line is the message itself. After the message, leave a blank line, and then type out the body or explanation including details about why the commit is needed (e.g. URL links).*

[Udacity Commit Message Style Guide](https://udacity.github.io/git-styleguide/)


## `.gitignore`

*If you want to keep a file in your project's directory structure but make sure it isn't accidentally committed to the project, you can use the specially named file, `.gitignore`*

*Globbing lets you use special characters to match patterns/characters. In the .gitignore file, you can use the following:*

 - blank lines can be used for spacing
 - `#` marks line as a comment
 - `*` matches 0 or more characters
 - `?` matches 1 character
 - `[abc]` - matches a, b, or c
 - `**` - matches nested directories - `a/**/z` matches
   - a/z
   - a/b/z
   - a/b/c/z



 - [Ignoring files from the Git Book](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files)
 - [gitignore from the Git Docs](https://git-scm.com/docs/gitignore#_pattern_format)
 - [Ignoring files from the GitHub Docs](https://help.github.com/articles/ignoring-files/)
 - [gitignore.io](https://www.gitignore.io/)

## Terms

**Version Control System (VCS)** or **Source Code Manager (SCM)**: A VCS allows you to:
revert files back to a previous state, revert the entire project back to a previous state,
review changes made over time, see who last modified something that might be causing
a problem, who introduced an issue and when, and more.

**Commit (snapshot)**: Git thinks of its data like a set of snapshots of a mini file system.
Every time you commit, or save the state of your project in Git, it basically takes a
picture of what all your files look like at that moment and stores a reference to that
snapshot.

**Repository (repo)**: A directory that contains your project work, as well as a few files
(hidden by default in Mac OS X) which are used to communicate with Git. Repositories
can exist either locally on your computer or as a remote copy on another computer.

**Working Directory**: The files that you see in your computer's file system. When you
open your project files up on a code editor, you're working with files in the Working
Directory.
This is in contrast to the files that have been saved (in commits!) in the repository.
When working with Git, the Working Directory is also different from the command line's
concept of the current working directory which is the directory that your shell is
"looking at" right now.

**Checkout**: When content in the repository has been copied to the Working Directory. It
is possible to checkout many things from a repository; a file, a commit, a branch, etc.

**Staging Area** or **Staging Index** or **Index**: A file in the Git directory that stores
information about what will go into your next commit. You can think of the staging area
as a prep table where Git will take the next commit. Files on the Staging Index are
poised to be added to the repository.

**SHA**: A SHA is basically an ID number for each commit. It is a 40-character string
composed of characters (0–9 and a–f) and calculated based on the contents of a file or
directory structure in Git. "SHA" is shorthand for "SHA hash". A SHA might look 
like this:

`e2adf8ae3e2e4ed40add75cc44cf9d0a869afeb6`

**Branch**: A branch is when a new line of development is created that diverges from the
main line of development. This alternative line of development can continue without
altering the main line.

Going back to the example of save point in a game, you can think of a branch as where
you make a save point in your game and then decide to try out a risky move in the
game. If the risky move doesn't pan out, then you can just go back to the save point. The
key thing that makes branches incredibly powerful is that you can make save points on
one branch, and then switch to a different branch and make save points there, too.

