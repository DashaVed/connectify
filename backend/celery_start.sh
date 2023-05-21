# shellcheck disable=SC2164
cd src
celery -A main worker --pool=solo -l info