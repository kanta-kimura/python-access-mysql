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
