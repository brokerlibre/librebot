from python:3.6-slim

run apt update && apt install -y git gcc make curl

run python -m pip install --upgrade pip

add ./bot.requirements.txt /tmp

run pip install -r /tmp/bot.requirements.txt
run python -c "import nltk; nltk.download('stopwords');"

add ./bot /bot
add ./scripts /scripts

workdir /bot

env ROCKETCHAT_URL=rocketchat:3000         \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ROCKETCHAT_ADMIN_USERNAME=admin        \
    ROCKETCHAT_ADMIN_PASSWORD=liberty      \
    ROCKETCHAT_BOT_USERNAME=libre          \
    ROCKETCHAT_BOT_PASSWORD=libre          \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash

cmd python /scripts/bot_config.py -r $ROCKETCHAT_URL                        \
           -an $ROCKETCHAT_ADMIN_USERNAME -ap $ROCKETCHAT_ADMIN_PASSWORD    \
           -bu $ROCKETCHAT_BOT_USERNAME -bp $ROCKETCHAT_BOT_PASSWORD     && \
    make train && make run-rocketchat
