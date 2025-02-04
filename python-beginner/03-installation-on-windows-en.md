# Installation on Windows / Macos / and setting up Pycharm

Download from <https://python.org>

during installation, check the option "Add Python 3.x to PATH"


<!--
why not use windows store version?

- does not automatically resolve the maximum path limit (260 characters)
  manual fix: regedit: set `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\LongPathsEnabled` to `1`
- does not put executables on PATH (instead of "flask" we have to run "python -m flask")
-->

## Installation on Windows

open an administrator privilege shell (like terminal) start menu. type in terminal. right click run as administrator

type in
```sh
wsl --install
```
after this reboot

again: open an administrator privilege shell (like terminal) start menu. type in terminal. right click run as administrator

```sh
wsl --install -d Ubuntu
```
you get a question about username and password.
for both use your `ruisnaam`

## Setup Ubuntu Windows

When done. open start menu and type ubuntu. Click on it.
You are now presented with a new shell. Type the following

```sh
sudo apt update
sudo apt upgrade
sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
press Y when asked.

## Setup Pyenv

now we install `pyenv`
```sh
curl -fsSL https://pyenv.run | bash
```
when its done we do the following
```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
```
## Setup Pyenv pt2
close your ubuntu shell and start a new one.
check if pyenv gives output. you should see the following

```sh
pyenv
pyenv 2.5.1
Usage: pyenv <command> [<args>]
```

then we install a new python interpreter

## Setup Pyenv pt3
```sh
pyenv install 3.13.0
```
then we set the global python interpreter
```sh
pyenv global 3.13.0
```

--- nieuwe steps vanaf Jan  Eelke heeft deze al gedaan
## Setup uv 
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null 2>&1
```

## hoe kom je bij je ubuntu files

- folder heet linux -> ubuntu  zo kom je vanuit windows bij all je subsystem files.


## Setup Pycharm

download url
- https://www.jetbrains.com/pycharm/

During installation you get a windows with certain install options:
- update context menu: yes
- create associations: yes
- update PAth variable: yes

when all is said and done we open Pycharm

we go to settings -> project -> python interpreter -> add interpreter (to the top right) -> on wsl
now we look carefully. ill show you the path to the python interpreter.

when we have selected the interpreter we press ok. and we are done.
then we go to settings new project -> python -> create new project -> select the interpreter we just added -> create
make sure to name the project  python-cursus-niels.

then again we go to settings -> type in the top left search bar. shell path. it should go to and highlight this field.
we type in:  wsl.exe

when we have done this we can start coding.


new project.  locatie veranderen naar \\wsl.localhost\Ubuntu\home\username\git\my_firstproject

vink niet aan create git repo en ook neit create welcome script

interpreter type custom environment.
type python
python path (hierin zou je zichtbaar \home\user\bin\python moeten zien staan.)


makefile aanpassen zodat pytho nenv geactiveerd wordt.

open de exercisees repo. settings. interpreter. add exising. navigeer naar folder maar in windows moet je een . zetten om de hidden venv folder te zien.


## git.kpn.org

2 repos we need for the course
- python-cursus
- python-cursus-exercises


## Getting the exercises repo

klik project. dan computer met pijltje naar beneden .switch van ssh naar http
git clone url   gevolgd door je werkplek username en wachtwoord.
vervolgens moet ie downloaden.

We will use git to get the exercises repository that i made.
We are going to use "Git" for this.  (dont be afraid we will only use git pull and git update when needed)

- git clone      (downloads a copy of a project that you or someone else created)
- git pull       (updates the project with the latest changes) 

In WSL (or on mac) we create a new dir called: git
- my personal recommendation for this is to create a new folder in your home dir called git
- yes there are some people that object to this but for now it is fine.

```sh

```
