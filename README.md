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

Coverage report:
```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
app/__init__.py       0      0   100%
app/main.py          35     15    57%   27-50, 59
app/tests.py          8      0   100%
-----------------------------------------------
TOTAL                43     15    65%
```

Lines 27-50 and 59 clearly do run, otherwise the test would not pass. You can
also verify this with a debugger.
