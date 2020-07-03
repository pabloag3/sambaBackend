# sambaBackend

## Descripción técnica del backend
### Tecnologías utilizadas
* Python, Django, Django Rest Framework
* Postgres

### Observaciones
#### Instalación de librerías en entorno virtual
Debe instalar los módulos especificados en el archivo *requirements.txt* ejecutando el comando
```
pip install -r requirements.txt
```

#### Archivo de varialbes de entorno
Se debe definir las siguientes variables de entorno en un archivo *.env*, ubicado en donde se encuentre el archivo *settings.py*, o bien, definirlas como variables de entorno en el sistema operativo. 
```
# SERVER CONFIG
DEBUG=True
SECRET_KEY=<su_clave_secreta>

# BD
BD_ENGINE=django.db.backends.postgresql
BD_NAME=samba
BD_USER=postgres
BD_PASS=postgres
BD_HOST=localhost
BD_PORT=5432
```