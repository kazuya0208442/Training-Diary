# mainのnginxのimageではないが、セキュリティ上問題となるrootユーザーでの実行を避けることができる。
FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

# Switches to the root user in order to manage files and configuration
USER root

# Runs some commands which create a new directory for our static volume, sets permissions, creates an empty file for default.conf, sets the ownership of this file to the nginx user (required so the envsubst can replace the file at runtime), makes the run.sh script executable.
RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

# Exposes /vol/static as a volume
VOLUME /vol/static

# Switches back to the nginx user
USER nginx

# Runs the run.sh script
CMD ["/run.sh"]

# proxy を起動するための shell script を書く。
# set -e は、もし何か実行に関して不具合が生じたら、scriptが実行されないようにするためのもの。debugingに役立つ。
# envsubst は、ファイルの中の環境変数の代わりになるものを指定。
# nginx -g 'daemon off;' は、nginxを起動させるコマンド。daemon offは、処理をforegroundで行うように設定している。
# これは、Dockerを使う時に推奨されている方法で、コンソールで出力結果が見れるようにするためのもの。


