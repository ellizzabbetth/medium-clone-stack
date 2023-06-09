Run:
docker compose -f local.yml up --build -d --remove-orphans

Down:
docker compose -f local.yml down


Logs:
docker compose -f local.yml logs <api_service>

Mailhog
localhost:8025 


docker volume inspect src_local_postgres_data

To view existing db backups:
docker compose -f local.yml exec postgres backup
docker compose -f local.yml exec postgres restore <backupfile>


Windows Subsystem
https://serverspace.io/support/help/python-3-virtual-environment-on-ubuntu-22-04/



python manage.py startapp users



That’s a short process for debugging a Docker Compose deployment
While this hasn’t been the most in-depth of guides on how to debug a Docker Compose-based deployment, it’s covered the essentials. To summarise, follow these steps to debug a Docker Compose-based container configuration:

Use docker-compose ps to see the state of all the containers
Use docker-compose logs to inspect the logs to find out what errors are occurring
Fix the problem
Restart the containers
Lather, rinse, repeat