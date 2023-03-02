#I had to use shlex on top of the run call because my command was too complex for the subprocess alone to understand.
# 
import subprocess
import shlex
import os


oldBitbucket = "https://bitbucket.it-economics.de/"
newBitbucket = "https://bitbucket-drvtwo.it-economics-testing.de/"

directory = "newDirWithPython"

gitRepoOrigin = f"{oldBitbucket}scm/it/customization.git"
gitRepoNew = f"{newBitbucket}scm/proj/customization.git"


git_cloneMirror = f"git clone --mirror {gitRepoOrigin} {directory}"
git_tag = "git tag"
git_branch = "git branch -a"
git_remove_origin = "git remote rm origin"
git_add_new_origin = f"git remote add origin {gitRepoNew}"
git_push = "git push origin --all"
git_push_tags = f"git push --tags"


p1 = subprocess.run(shlex.split(git_cloneMirror))
os.chdir(f"{directory}")

p2 = subprocess.run(shlex.split(git_tag))

p3 = subprocess.run(shlex.split(git_branch))

p4 = subprocess.run(shlex.split(git_remove_origin))

p5 = subprocess.run(shlex.split(git_add_new_origin))

p6 = subprocess.run(shlex.split(git_push))

p7 = subprocess.run(shlex.split(git_push_tags))
