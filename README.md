```
python3 -m venv venv
pip install -r requirements.txt
```

I can't just use SQLite because we need an async DB driver. The exact steps
migth vary depending on your system / Postgres setup.
```
sudo -u postgres createuser test
sudo -u postgres createdb test -O test
echo "ALTER ROLE test PASSWORD 'test'"|sudo -u postgres psql
```

```
./runtests.sh
```
