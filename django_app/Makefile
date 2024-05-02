test:
	docker-compose up -d db minio
	poetry run pytest tests --ds redbox_app.settings -v --cov=redbox_app.redbox_core --cov-fail-under 60 -o log_cli=true

