# coding: utf-8

class Twitter():

    LIMIT = 30
    API_HOST = "https://api.twitter.com/1.1/"

    def __init__(self,client, token, secret):
        self.client = client
        self.token = token
        self.secret = secret

    def get_timeline(self, since_id = None, max_id = None):
        url = "{}statuses/home_timeline.json".format(self.API_HOST)
        params = { "count": self.LIMIT }
        if since_id:
            params["since_id"] = since_id
        if max_id:
            params["max_id"] = since_id
        return self.client.make_request(url, self.token, self.secret, params, protected=True)
