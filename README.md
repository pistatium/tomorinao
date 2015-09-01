# TomoriNao
TomoriNao is a joke twitter client, changes all username to 友利奈緒(Tomori Nao)

## Deployment(WIP)

### Require
    * GoogleAppEngine SDK

```
git submodule init
mkvirtualenv --system-site-packages --distribute --python=python2.7 tomorinao
pip install -r requirements.txt -t libraries
dev_appserver.py .
open localhost:8080
```
