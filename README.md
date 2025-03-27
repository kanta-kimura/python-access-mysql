## mysql を docker で構築

### Start Container

```zsh
docker-compose up -d
```

### DB Access

```zsh
mysql -h 127.0.0.1 -P 53306 -u user -p
```

### 参考

https://zenn.dev/ryo7/articles/create-mysql-on-docker

## さくらに pip をインストール

ssh 接続して、下記を実行

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

## SQLAlchemy

https://qiita.com/arkuchy/items/75799665acd09520bed2
