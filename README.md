# すべてが友利になる
TomoriNao is a joke twitter client, changes all username to 友利奈緒(Tomori Nao)

http://tomorinao.kimihiro-n.appspot.com/

## Deployment

### Require
    * GoogleAppEngine SDK

```
git submodule init
pip install -r requirements.txt -t libraries
cp src/setting.py.orig src/setting.py
#Edit setting.py
#Edit app.yaml
appcfg.py update .
```
