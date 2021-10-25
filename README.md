# 掃除しなくちゃ - WebApp/Backend

`F_2104`(`Undefined`)：「掃除しなくちゃ」のバックエンドサーバーです

## 開発環境の構築

1. GitHubからClone
   ```git clone https://github.com/jphacks/F_2104.git -b dev_backend```

   でcloneできます

2. Python 3.9.nのインストール
   パッケージの都合からpython 3.9で開発してるので，python3.9用の環境構築をお願いします．[pyenv](https://github.com/pyenv/pyenv)で環境構築すると楽です．

3. venv
   わかるならvenv使うと開発環境が汚くなりにくいですが，わかんないなら特に気にしなくていいです．

4. pipパッケージのインストール
   ```pip install -r requirements.txt```

5. 開発ファイル
   とりあえず認証系の一部・PostgreSQLの接続設定はそれぞれ分けてますがそれ以外は`app.py`にいます．

6. PostgreSQL
   インストール方法はPotgreSQL　インストールって調べたら出てくると思います．
   とりあえずrole名：`souji`
   パスワード：`soujipassword`
   データベース名：`sensor_data`
   になっています．よくわかんなかったら次の手順でやってください．（.envいじってもらって任意の設定をしてもらってもOKです）
   ```zsh
   $ psql
   postgres=# CREATE ROLE souji SUPERUSER LOGIN PASSWORD 'soujipassword';
   CREATE ROLE
   postgres=# CREATE DATABASE sensor_data;
   CREATE DATABASE
   ```
   
   そしてTable情報を流し込んでください．
   ```bash
   $ psql -d sensor_data -f main.sql
   ```


## メモ

1. Push先

   直接このRepoにPushしてもらってもOKです．

1. Pull Request(PR)

   自分のRepoからこのRepoにPRしてもらってもOKです．ただし，このBranchをmainへPRするとかはしないでください！

1. Issue

   Issueのご確認お願いします．実装次第閉じてもらうか，確認次第閉じておきます．
