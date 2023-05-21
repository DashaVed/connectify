# shellcheck disable=SC2164
cd src
celery -A main beat -l INFO