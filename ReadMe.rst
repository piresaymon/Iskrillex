To Rotate Locally the IsKrillex;
Follow the instruction of the links below;
Note: it is not necessary to go to the next page, ie for each completed skip to the next step
link, and not the next page link;

Recommends Linux Mint >= 16 Version

Pre-requirements:
Having a heroku account

https://signup.heroku.com/login
===============================

After creating your account you must install the Heroku Toolbelt

https://toolbelt.heroku.com/
============================

Rotated Locally requirements:
Step 1:

https://devcenter.heroku.com/articles/getting-started-with-python#introduction
==============================================================================

You must install the python 2, each according to its operating system platform, in the case of Linux mostly already been installed. To check if it is installed just open the terminal of your choice and digital command

python --version
================

Soon then you must install the python pip, search the internet the right way for each operating system if you are using versions of Linux Ubuntu or its derivatives follows the installation commands;

Install pip and virtualenv for Ubuntu 10.10 Maverick and newer
New systems equal or greater than the Ubuntu 10.10

 sudo apt-get install python-pip python-dev build-essential
 sudo pip install --upgrade
 sudo pip install --upgrade virtualenv
================================================== ==========

New systems to lower the Ubuntu 10.10
For older versions of Ubuntu

Install Easy Install

 sudo apt-get install python-setuptools python-dev build-essential
================================================== ==========

Install pip

 sudo easy_install pip
================================================== ==========

Install virtualenv

sudo pip install --upgrade virtualenv
======================================
Finally install the latest available version of Postgres, corresponding to your operacional.Exemplo system: Linux Mint 17 Rose

sudo apt-get install postgresql-9.3 *
=====================================

Now you are ready to install and Virtualenv Create your directory Isolated;

Note: Virtualenv is important for applications that tenhão specific features tests, in which they are installed do not conflict with other projetos.Exemplo the IsKrillex uses django 1.4.22, if another project nessecitar django 1.9, we would have a problem, because the new django installed remove the previous, regardless of version.
using Virtualenv poderar you test your application and its dependencies without the risk of interfering with their other projects.

Enter the folder where the Iskrillex project and start the process with the Virtualenv

pip install virtualenv
=======================

Note: you just installed virtualenv the system;
So Enable virtualenv in the project:

If you are using Windows, run the following command:

venv\Scripts\activate.bat
==========================

If not using Window, run the following command:

source venv/bin/activate
==========================

At this point your this isolated system folder and can now install the project dependency; With the command:

pip install -r requirements.txt
================================

The application is almost ready to start locally. Django uses local resources, so first, you will need to run collectstatic:

python manage.py collectstatic
==============================

Respond with yes.

Now start your application locally using heroku site, which was installed as part of the set of Toolbelt: With the command.

heroku web site
===================

Ready now just open your preferancia browser and type:

http://localhost:5000/
=======================

for terminating the terminal press Ctrl + C


