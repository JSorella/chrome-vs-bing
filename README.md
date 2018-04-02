# google-vs-bing

El propósito de este proyecto es el de automatizar tests en Google y en Bing usando Selenium 
y mostrar sus diferencias en Behave.

## Dependencias

Este proyecto requiere de las siguientes dependencias:

1. behave
2. selenium

## Ejecución de los tests

Para ejecutar los tests, hay dos opciones:

1. Usando el comando `behave` en la terminal 
2. Corriendo los tests desde PyCharm

## Manejo de Entornos en Python _(opcional)_

Para manejar las dependencias de un entorno en Python, hay una herramienta llamada “VirtualenvWrapper”:
http://virtualenvwrapper.readthedocs.io/en/latest/install.html

Para instalarlo:
    
    $ pip install virtualenvwrapper

Después hay que abrir el archivo ~/.bashrc y se le debe agregar las siguientes lineas al final:

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

Finalmente, recargar el archivo de startup haciendo:

    $ source ~/.bashrc

Para verificar si quedó bien instalado, ejecutar el comando:
    
    $ workon    

Debería no devolver nada.
Cada vez que ejecutemos este comando, listará los environments existentes dentro de nuestra máquina local.
Para crear un nuevo entorno para nuestro proyecto, corremos el siguiente comando:

    $ mkvirtualenv <nombre_de_nuestro_proyecto>

(El nombre de nuestro proyecto debe ser el mismo que en Pycharm)

Si todo salió bien, deberíamos verlo listado al ejecutar el comando workon.
Para seleccionar nuestro nuevo entorno, ejecutamos el comando:

    $ workon <nombre_de_nuestro_proyecto>

Ahora, debemos instalar aquellas dependencias propias de nuestro entorno:

    $ pip install selenium
    $ pip install behave
