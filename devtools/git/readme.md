# Git

## Resources

 - [Git Internals - Plumbing and Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
 - [Customizing Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
 - [Git Basics - Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
 - [Inspecting a repository](https://www.atlassian.com/git/tutorials/inspecting-a-repository)
 - [Git Basics - Tagging from the Git Book](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
 - [Git Tag from the Git Docs](https://git-scm.com/docs/git-tag)
 - [Ignoring files from the Git Book](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files)
 - [gitignore from the Git Docs](https://git-scm.com/docs/gitignore#_pattern_format)
 - [Ignoring files from the GitHub Docs](https://help.github.com/articles/ignoring-files/)
 - [gitignore.io](https://www.gitignore.io/)
 - [Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
 - [Learn Git Branching](http://learngitbranching.js.org/)
 - [Git Branching Tutorial](https://www.atlassian.com/git/tutorials/using-branches)
 - [Basic Merging from Git Book](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#Basic-Merging)
 - [git merge from Atlassian blog](https://www.atlassian.com/git/tutorials/git-merge)
 - [Basic Merge Conflicts from the Git book](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#Basic-Merge-Conflicts)
 - [How Conflicts Are Presented from the Git docs](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented)
 - [git revert Atlassian tutorial](https://www.atlassian.com/git/tutorials/undoing-changes)
 - [Reset Demystified from Git Blog](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)
 - [Ancestry References from Git Book](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#Ancestry-References)
 - [Working with Remotes from the Git book](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes#_showing_your_remotes)
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

#### init

`git init` - Creates an empty Git repository [Docs](https://git-scm.com/docs/git-init)

#### clone

`git clone` - Clone a repository into a new directory [Docs](https://git-scm.com/docs/git-clone)

#### status

`git status`- [Docs](https://git-scm.com/docs/git-status)

#### log

`git log` - Shows the commit logs. [Docs](https://git-scm.com/docs/git-log)

`git log --oneline` - Display file changes summary

`git log -p` - Display actual file changes

`git log --oneline --decorate --graph --all`

`git log --author=<name>` - Filter commits by author

`git log --grep=<regex>` - Filter by regex

`git shortlog` - Displays an alphabetical list of names and the commit messages

`git shortlog -s` - Show just the number of commits

`git shortlog -sn` - Sort numerically

`git show <SHA>` - Show details of a commit


#### add

`git add <file>` - Move files from the Working Directory to the Staging Index (Stage)

`git add .` - Stage all files in the current directory

#### rm

`git rm --cached <file>` - Move a file from the Staging Index back to the Working Directory (Unstage)

#### commit

`git commit` - Commit changes to the repository
`git commit -m '<message>'` - Commit with message
`git commit --amend` - Alter the most-recent commit

#### diff

`git diff` - See changes that have been made but haven't been committed [Docs](https://git-scm.com/docs/git-diff)

#### tag

`git tag <tag>` - Add a lightweight tag to a commit

`git tag -a <tag>` - Add an annotated tag to a commit

`git tag -d <tag>` - Delete a tag

`git tag <tag> <SHA>` - Add tag to specified commit

#### branch

`git branch` - List branches

`git branch <branch>` - Make a branch

`git branch <branch> <SHA>` - Make a branch starting from specified commit

`git branch -d <branch>` - Delete a branch

`git branch -D <branch>` - Delete a branch (force)

`git branch --set-upstream-to <remote>/<branch>` - Set upstream for the current branch

#### checkout

`git checkout <branch>` - Switch to a branch

`git checkout -b <branch>` - Create branch and switch to it

#### merge

`git merge <branch>` - Merge specified branch into current branch [Docs](https://git-scm.com/docs/git-merge)


#### revert

`git revert <SHA>` - Revert changes of specified commit [Docs](https://git-scm.com/docs/git-revert)

#### reset

`git reset <SHA>` - Reset (erase) commits [Docs](https://git-scm.com/docs/git-reset)

`git reset <SHA> --mixed` - Move changes to Working Directory

`git reset <SHA> --soft` - Move changes to Staging Index

`git reset <SHA> --hard` - Move changes to Trash


#### remote

`git remote` - List remote repositories [Docs](https://git-scm.com/docs/git-remote)

`git remote -v` - List remotes with URL

`git remote add <remote> <URL|SSH>` - Add remote with specified shortname (usually *origin*)

#### push

`git push` - Send local commits to a remote repository **upstream**

`git push <remote> <branch>` - Push to specified remote branch

`git push -u <remote> <branch>` - Push and set as **upstream**

#### pull

`git pull` - Fetch and merge remote commits from **upstream**

`git pull <remote> <branch>` - Pull specified remote branch

#### fetch

`git fetch` - Fetch remote commits from all branches without merging

`git fetch <remote> <branch>` - Fetch commits for specified remote branch


## Commit Messages

*The best way that I've found to come up with a commit message is to finish this phrase, "This commit will...". However, you finish that phrase, use that as your commit message.*


*When you're writing the commit message, the first line is the message itself. After the message, leave a blank line, and then type out the body or explanation including details about why the commit is needed (e.g. URL links).*

[Udacity Commit Message Style Guide](https://udacity.github.io/git-styleguide/)

## Tags

*In the command above (git tag -a v1.0) the -a flag is used. This flag tells Git to create an annotated flag. If you don't provide the flag (i.e. git tag v1.0) then it'll create what's called a lightweight tag.*

*Annotated tags are recommended because they include a lot of extra information such as:*

 - *the person who made the tag*
 - *the date the tag was made*
 - *a message for the tag*


## Merge

There are two types of merges:

 - Fast-forward merge – the branch being merged in must be ahead of the checked out branch. The checked out branch's pointer will just be moved forward to point to the same commit as the other branch.
 - the regular type of merge
   - two divergent branches are combined
   - a merge commit is created

### Merge Conflict Indicators Explanation
The editor has the following merge conflict indicators:

 - `<<<<<<< HEAD` everything below this line (until the next indicator) shows you what's on the current branch
 - `|||||||` merged common ancestors everything below this line (until the next indicator) shows you what the original lines were
 - `=======` is the end of the original lines, everything that follows (until the next indicator) is what's on the branch that's being merged in
 - `>>>>>>>` heading-update is the ending indicator of what's on the branch that's being merged in (in this case, the heading-update branch)

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


## Relative Commit References

*You already know that you can reference commits by their SHA, by tags, branches, and the special HEAD pointer. Sometimes that's not enough, though. There will be times when you'll want to reference a commit relative to another commit. For example, there will be times where you'll want to tell Git about the commit that's one before the current commit...or two before the current commit. There are special characters called "Ancestry References" that we can use to tell Git about these relative references. Those characters are:*

 - `^` indicates the parent commit
 - `~` indicates the first parent commit

Here's how we can refer to previous commits:

 - the parent commit – the following indicate the parent commit of the current commit
   - HEAD^
   - HEAD~
   - HEAD~1
 - the grandparent commit – the following indicate the grandparent commit of the current commit
   - HEAD^^
   - HEAD~2
 - the great-grandparent commit – the following indicate the great-grandparent commit of the current commit
   - HEAD^^^
   - HEAD~3

*The main difference between the ^ and the ~ is when a commit is created from a merge. A merge commit has two parents. With a merge commit, the ^ reference is used to indicate the first parent of the commit while ^2 indicates the second parent. The first parent is the branch you were on when you ran git merge while the second parent is the branch that was merged in.*

## Remote Repository

*Git is a distributed version control system which means there is not one main repository of information. Each developer has a copy of the repository. So you can have a copy of the repository (which includes the published commits and version history) and your friend can also have a copy of the same repository. Each repository has the exact same information that the other ones have, there's no one repository that's the main one.*

Local refs: `<remote-shortname>/<branch>`

Fetch changes and merge:

```
git pull origin master
```

Fetch changes and merge manually:

```
git fetch origin master
git merge origin/master
```


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

