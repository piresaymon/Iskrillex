Para Rodar Localmente a iskrillex;
Siga as instrução dos links abaixo;
Nota: não é necessario ir para a proxima pagina, ou seja para cada etapa completada pule para o proximo
link, e não para a proxima pagina do link;

Pre-Requisitos:
Ter uma conta heroku
https://signup.heroku.com/login
============================================================
Após cria sua conta tu deves instalar o Heroku Toolbelt
https://toolbelt.heroku.com/
============================================================
Requisitos de Rodar Localmente:
Passo 1:
https://devcenter.heroku.com/articles/getting-started-with-python#introduction
============================================================
Voce deve instalar segundo o link o python, cada um segundo a sua plataforma de sistema operacional, no caso do linux em sua maioria ja vem instalado. Para conferir se está instalado basta abrir o terminal de sua preferencia e digital o comando
python --version
============================================================
Logo em seguida voce deve instalar o pip do python, busque na internet a forma correta para cada sistema operacional, caso esteja usando versões do Linux Ubuntu ou seus derivados segue os comandos de instalação;

Install pip and virtualenv for Ubuntu 10.10 Maverick and newer
Novos Sistemas iguais ou superiores a o Ubuntu 10.10 

 sudo apt-get install python-pip python-dev build-essential 
 sudo pip install --upgrade pip 
 sudo pip install --upgrade virtualenv 
============================================================

Novos Sistemas inferiores a o Ubuntu 10.10
For older versions of Ubuntu

Install Easy Install
 sudo apt-get install python-setuptools python-dev build-essential 
============================================================
Install pip
 sudo easy_install pip 
============================================================
Install virtualenv
sudo pip install --upgrade virtualenv 
============================================================

Por fim instale a ultima versão disponivel do Postgres, correspondente a seu sistema operacional.Exemplo:Linux Mint 17 Rosa
sudo apt-get install postgresql-9.3*
============================================================

Agora você está pronto pra instalar o Virtualenv e Criar o seu diretorio Isolado;

Nota: o Virtualenv é importante para testes de aplicações que tenhão recursos especificos, nos quais se forem instalados não entrem em conflito com outros projetos.Exemplo a IsKrillex utiliza django 1.4.22, se um outro projeto nessecitar de django 1.9, teriamos um problema, pois o novo django instalado removeria o anterior, independente da versão.
utilizando Virtualenv você poderar testar seu aplicativo e suas dependencias sem correr o risco de interferir no seus outro projetos.

Entre na Pasta onde se encontra o projeto Iskrillex e inicie o processo com o Virtualenv
 pip install virtualenv 
 ============================================================
 Note: voce acabou de instalar o virtualenv no sistema;
 Então, Ative o  virtualenv no projeto:
 
Se estiver usando  Windows, rode o seguinte comando:

venv\Scripts\activate.bat
============================================================
Se não estiver usando  Window, rode o seguinte command:
source venv/bin/activate

Nesse momento a sua pasta esta isolado do sistema e agora podemos instalar as dependencia do projeto; Com o comando:
pip install -r requirements.txt
============================================================
O aplicativo está quase pronto para iniciar localmente. Django usa recursos locais, por isso, em primeiro lugar, você vai precisar executar collectstatic:
python manage.py collectstatic
============================================================
Responda com yes.

Agora inicie a sua aplicação localmente usando heroku local, que foi instalado como parte do conjunto de  Toolbelt:Com o comando.
heroku local web
============================================================
Pronto agora basta abrir seu navegador de preferancia e digitar:
http://localhost:5000
============================================================
para encerra o processo no terminal pressione Ctrl+C 




 






























Facebook/Heroku sample app -- Python
====================================

This is a sample app showing use of the Facebook Graph API, written in
Python, designed for deployment to Heroku_.

.. _Heroku: http://www.heroku.com/

Run locally
-----------

Set up a Virtualenv and install dependencies::

    virtualenv --no-site-packages env/
    source env/bin/activate
    pip install -r requirements.txt

`Create an app on Facebook`_ and set the Website URL to
``http://localhost:5000/``.

Copy the App ID and Secret from the Facebook app settings page into
your ``.env``::

    echo FACEBOOK_APP_ID=12345 >> .env
    echo FACEBOOK_SECRET=abcde >> .env

Launch the app with Foreman_::

    foreman start

.. _Create an app on Facebook: https://developers.facebook.com/apps
.. _Foreman: http://blog.daviddollar.org/2011/05/06/introducing-foreman.html

Deploy to Heroku via Facebook integration
-----------------------------------------

The easiest way to deploy is to create an app on Facebook and click
Cloud Services -> Get Started, then choose Python from the dropdown.
You can then ``git clone`` the resulting app from Heroku.

Deploy to Heroku directly
-------------------------

If you prefer to deploy yourself, push this code to a new Heroku app
on the Cedar stack, then copy the App ID and Secret into your config
vars::

    heroku create --stack cedar
    git push heroku master
    heroku config:add FACEBOOK_APP_ID=12345 FACEBOOK_SECRET=abcde

Enter the URL for your Heroku app into the Website URL section of the
Facebook app settings page, hen you can visit your app on the web.
