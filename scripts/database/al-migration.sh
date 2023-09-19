#!/bin/bash

# マイグレーションファイルを作成するコマンド

# -m はマイグレーションファイルの名前

while getopts m: OPT
do
  case $OPT in
    m) NAME=$OPTARG
       ;;
  esac
done

cd /workspace/db && \
if [ -z "$NAME" ]; then
  poetry run alembic revision --autogenerate
else
  poetry run alembic revision --autogenerate -m "$NAME"
fi