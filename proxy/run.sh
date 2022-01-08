# proxy を起動するための shell script を書く。
# set -e は、もし何か実行に関して不具合が生じたら、scriptが実行されないようにするためのもの。debugingに役立つ。
# envsubst は、ファイルの中の環境変数の代わりになるものを指定。
# nginx -g 'daemon off;' は、nginxを起動させるコマンド。daemon offは、処理をforegroundで行うように設定している。
# これは、Dockerを使う時に推奨されている方法で、コンソールで出力結果が見れるようにするためのもの。



#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'