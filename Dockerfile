# イメージが軽く、安定性があるバージョンを選ぶ
FROM python:3.9-alpine3.13

# Pythonの出力がコンテナのログに送られるように設定する。
ENV PYTHONUNBUFFERED 1

# requirements.txtをイメージの中にコピーする。
COPY ./requirements.txt /requirements.txt
# app directory をイメージへコピーする。
COPY ./app /app
# 
COPY ./scripts /scripts
# Doxker image のコマンドの実行を、/app から行うように設定する。
WORKDIR /app
# 8000 port を開ける
EXPOSE 8000

# image layer を小さくするためにRUNコマンドを1回でまとめる。RUNコマンドごとにlayerが作られてしまうから。

RUN python -m venv /py && \
    # /py に仮想環境を作る。
    # pipを最新バージョンにupgrade
    /py/bin/pip install --upgrade pip && \
    # apk を使って、postgresql-client をインストールする。DjangoのdriverがPostgresSQLにアクセスできるようにするため。
    apk add --update --no-cache postgresql-client && \
    # build-base, postgresql-dev, musl-dev はdriverのインストールに必要な依存関係にあるもの。
    # linux-headersはpipを通してuWSGIをインストールするために必要。
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    # requirements.txtに書かれた依存関係にあるものをインストール
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    # 新しいユーザー app を追加する
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    # app user をownerにする。user:group
    chown -R app:app /vol && \
    # app user は、読み込み、書き込み、削除が可能。permissionの設定。
    chmod -R 755 /vol && \
    # /scripts directory を実行可能にする
    chmod -R +x /scripts

# /py の仮想環境にPATHを追加する。これにより、/py/bin/python　と毎回明記しなくて済む。
# /scripts directoryも追加する。
ENV PATH="/scripts:/py/bin:$PATH"

# image user をapp にする
USER app

# コンテナが起動したら、run.shを実行する。
CMD ["run.sh"]