superuser:
	./manage.py createsuperuser --username admin --email test@test.com

runserver:
	./manage.py runserver

migrate:
	./manage.py migrate

makemigrations:
	./manage.py makemigrations

shell:
	./manage.py shell

test:
	./manage.py test

docker-makemigrations:
	docker-compose run web python manage.py makemigrations

docker-migrate:
	docker-compose run web python manage.py migrate

docker-createsuperuser:
	docker-compose run web python manage.py createsuperuser

docker-collectstatic:
	docker-compose run web python manage.py collectstatic --noinput
