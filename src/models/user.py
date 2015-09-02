# coding: utf-8

from google.appengine.ext import ndb


class User(ndb.Model):
    screen_name = ndb.StringProperty()
    display_name = ndb.StringProperty()
    profile_image_url = ndb.StringProperty()
    token = ndb.StringProperty()
    secret = ndb.StringProperty()

    @classmethod
    def get_by_id(cls, unique_id):
        return cls.get_by_key_name(unique_id)

    @classmethod
    def load(cls, user_info):
        return cls(
            id = "{}:{}".format(user_info["service"], user_info["id"]),
            screen_name = user_info["username"],
            display_name = user_info["name"],
            profile_image_url = user_info["picture"],
            token = user_info["token"],
            secret = user_info["secret"]
        )
