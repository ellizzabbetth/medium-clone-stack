Run:
docker compose -f local.yml up --build -d --remove-orphans
make build

Down:
docker compose -f local.yml down
make down-v

Logs:
docker compose -f local.yml logs <api_service>

Mailhog
localhost:8025 

Flowers:
http://localhost:5555/

docker volume inspect src_local_postgres_data
make volume

make authors-db
-- inside psql service
    \l
    \q
    \connect
    \dt
    \q

python3 -c "import secrets; print(secrets.token_urlsafe(38))"
pip install -r requirements/local.txt


To view existing db backups:
docker compose -f local.yml exec postgres backup
docker compose -f local.yml exec postgres restore <backupfile>


Windows Subsystem
https://serverspace.io/support/help/python-3-virtual-environment-on-ubuntu-22-04/



python manage.py startapp users


http://localhost:8000/redoc/
http://localhost:8080/supersecret/


That’s a short process for debugging a Docker Compose deployment
While this hasn’t been the most in-depth of guides on how to debug a Docker Compose-based deployment, it’s covered the essentials. To summarise, follow these steps to debug a Docker Compose-based container configuration:

Use docker-compose ps to see the state of all the containers
Use docker-compose logs to inspect the logs to find out what errors are occurring
Fix the problem
Restart the containers
Lather, rinse, repeat

ML NLP
https://www.kaggle.com/general/203318
https://www.geeksforgeeks.org/nlp-gensim-tutorial-complete-guide-for-beginners/
https://stackabuse.com/python-for-nlp-working-with-the-gensim-library-part-1/
https://radimrehurek.com/gensim/auto_examples/
https://docs.aws.amazon.com/sagemaker/latest/dg/lda.html