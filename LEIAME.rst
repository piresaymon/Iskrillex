Para Rodar Localmente a iskrillex!
===================================

Siga as instrução dos links abaixo;
Nota: não é necessario ir para a proxima pagina, ou seja para cada etapa completada pule para o proximo
link, e não para a proxima pagina do link;

Recomendado Linux Mint versões 16 ou superiores;

Pre-Requisitos:
Ter uma conta heroku

https://signup.heroku.com/login
===============================

Após cria sua conta tu deves instalar o Heroku Toolbelt

https://toolbelt.heroku.com/
============================

Requisitos de Rodar Localmente:
Passo 1:

https://devcenter.heroku.com/articles/getting-started-with-python#introduction
==============================================================================

Voce deve instalar segundo o python 2, cada um segundo a sua plataforma de sistema operacional, no caso do linux em sua maioria ja vem instalado. Para conferir se está instalado basta abrir o terminal de sua preferencia e digital o comando

python --version
============================================================

Logo em seguida você deve instalar o pip do python, busque na internet a forma correta para cada sistema operacional, caso esteja usando versões do Linux Ubuntu ou seus derivados segue os comandos de instalação;

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
======================================
Por fim instale a ultima versão disponivel do Postgres, correspondente a seu sistema operacional.Exemplo:Linux Mint 17 Rosa

sudo apt-get install postgresql-9.3*
=====================================

Agora você está pronto pra instalar o Virtualenv e Criar o seu diretorio Isolado;

Nota: o Virtualenv é importante para testes de aplicações que tenhão recursos especificos, nos quais se forem instalados não entrem em conflito com outros projetos.Exemplo a IsKrillex utiliza django 1.4.22, se um outro projeto nessecitar de django 1.9, teriamos um problema, pois o novo django instalado removeria o anterior, independente da versão.
utilizando Virtualenv você poderar testar seu aplicativo e suas dependencias sem correr o risco de interferir no seus outro projetos.

Entre na Pasta onde se encontra o projeto Iskrillex e inicie o processo com o Virtualenv
 pip install virtualenv 
 =======================
 Note: voce acabou de instalar o virtualenv no sistema;
 Então, Ative o  virtualenv no projeto:
 
Se estiver usando  Windows, rode o seguinte comando:

venv\Scripts\activate.bat
==========================

Se não estiver usando  Window, rode o seguinte command:

source venv/bin/activate
==========================

Nesse momento a sua pasta esta isolado do sistema e agora podemos instalar as dependencia do projeto; Com o comando:

pip install -r requirements.txt
================================

O aplicativo está quase pronto para iniciar localmente. Django usa recursos locais, por isso, em primeiro lugar, você vai precisar executar collectstatic:

python manage.py collectstatic
==============================

Responda com yes.

Agora inicie a sua aplicação localmente usando heroku local, que foi instalado como parte do conjunto de  Toolbelt:Com o comando.

heroku local web
===================

Pronto agora basta abrir seu navegador de preferancia e digitar:

http://localhost:5000
=======================

para encerra o processo no terminal pressione Ctrl+C 
