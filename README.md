# eng4021-33c-aula-git-giovana

python #inicializa a linguagem python no django/
import secrets #importa o módulo secrets do python que serve para gerar senhas aleatórias/
secrets.token_urlsafe(32) #gera uma senha aleatória de 32bytes, necessária para fazer a página web funcionar/
python3 manage.py #utilizado para permitir o uso de outras funcionalidade do tipo manage.py/
python manage.py startapp appGiovana #criar um app no diretório chamado appGiovana/
python3 manage.py makemigrations #cria arquivos de migração para o banco de dados com base nas classes que foram criadas no models.py/
python3 manage.py migrate #realiza de fato as migrações cridas na linha anterior/
python3 manage.py createsuperuser #cria um superusuário, que funciona como um administrador do site. Esse comando solicita um nome, email e senha para o superusuário/
