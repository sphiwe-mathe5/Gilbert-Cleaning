.PHONY:install
install:
	poetry install


.PHONY:install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install 


.PHONY: lint
lint:
	poetry run pre-commit run --all-files


.PHONY:migrate
migrate:
	poetry run python -m core.manage migrate


.PHONY:migrations
migrations:
	poetry run python -m core.manage makemigrations


.PHONY:runserver
runserver:
	poetry run python -m core.manage runserver


.PHONY:superuser
superuser:
	poetry run python -m core.manage createsuperuser


.PHONY:setup
setup: install migrations migrate install-pre-commit ;


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True
#EMAIL_HOST_USER = 'mathesphiwe689@gmail.com'
#EMAIL_HOST_PASSWORD = 'ruyn iact vzqe ppor'