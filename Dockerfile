# イメージが軽く、安定性があるバージョンを選択
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
# ローカル開発用のポートを8000番として、開放する。
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
    # adduser --disabled-password --no-create-home app && \

    # -p のオプションは、階層ディレクトリを作成する。
    mkdir -p app/vol/web/static && \
    mkdir -p app/vol/web/media && \

    # chownコマンドは、指定したファイルやディレクトリのユーザー所有権（所有者）やグループ所有権（グループ）を変更します。ユーザー所有権は、ユーザー名やユーザーIDで指定し、グループ所有権は、グループ名やグループIDで指定する。
    # -R オプションは、指定したディレクトリとそのディレクトリ以下のファイルやディレクトリの所有権を再帰的に変更する。
    # /vol 以下の全てのディレクトリやファイルのユーザー所有権を[app]、グループ所有権を[app]にする。
    # chown -R app:app app/vol/web && \

    # app user は、読み込み、書き込み、削除が可能。permissionの設定。
    # chmodコマンドは、ファイルやディレクトリのアクセス制御のモードを変更するコマンド
    # -R オプションは、ファイルやディレクトリのモードを再帰的に変更する。
    # 755 は、ユーザーが7(rwx)、グループが7(rwx)、その他のユーザーが5(r-x)
    # /vol 以下のすべてのディレクトリやファイルに対して、モード755を設定
    chmod -R 755 app/vol/web && \

    # /scripts directory を実行可能にする
    # +x は、実行権限の追加
    chmod -R +x /scripts

# /py の仮想環境にPATHを追加する。これにより、/py/bin/python　と毎回明記しなくて済む。
# /scripts directoryも追加する。
ENV PATH="/scripts:/py/bin:$PATH"

# image user をapp にする


# コンテナが起動したら、run.shを実行する。
# PATHに/scriptsを追加したので、/scripts/run.sh のようにフルパスを書かなくてもよくなった。
CMD ["run.sh"]