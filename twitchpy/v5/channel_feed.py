from twitchpy.other.constants import *
from twitchpy.other.decorators import oauth_required
from twitchpy.other.helper import dict_gen, parameter_check
from twitchpy.v5.base import TwitchBase


class ChannelFeed(TwitchBase):
    def get_multiple_feed_posts(
            self,
            channel_id,
            limit=None,
            cursor=None,
            comments=None):
        parameter_check(limit=limit, comments=comments)
        params = dict_gen(limit=limit, cursor=cursor, comments=comments)
        request = 'feed/{}/posts'.format(channel_id)
        return self._request(GET, request, params=params)

    @oauth_required
    def create_feed_post(self, channel_id, content, share=False):
        request = 'feed/{}/posts'.format(channel_id)
        params = dict_gen(share=share)
        json = dict_gen(content=content)
        return self._request(POST, request, json=json, params=params)

    @oauth_required
    def delete_feed_post(self, channel_id, post_id):
        request = 'feed/{}/posts/{}'.format(channel_id, post_id)
        return self._get(request)

    @oauth_required
    def create_feed_reaction(self, channel_id, post_id, emote_value):
        request = 'feed/{}/posts/{}/reactions'.format(channel_id, post_id)
        params = dict_gen(emote_id=emote_value)
        return self._post(request, params=params)

    @oauth_required
    def delete_feed_reaction(self, channel_id, post_id, emote_value):
        request = 'feed/{}/posts/{}/reactions'.format(channel_id, post_id)
        params = dict_gen(emote_id=emote_value)
        return self._delete(request, params=params)

    def get_feed_comments(self, channel_id, post_id, limit=None, cursor=None):
        parameter_check(limit=limit)
        request = 'feed/{}/posts/{}/comments'.format(channel_id, post_id)
        params = dict_gen(limit=limit, cursor=cursor)
        return self._get(request, params=params)

    @oauth_required
    def create_feed_comment(self, channel_id, post_id, content):
        request = 'feed/{}/posts/{}/comments'.format(channel_id, post_id)
        json = dict_gen(content=content)
        return self._post(request, json=json)

    @oauth_required
    def delete_feed_comment(self, channel_id, post_id, comment_id):
        request = 'feed/{}/posts/{}/comments/{}'.format(
            channel_id, post_id, comment_id)
        return self._delete(request)

    @oauth_required
    def create_feed_comment_reaction(
            self,
            channel_id,
            post_id,
            comment_id,
            emote_value):
        request = 'feed/{}/posts/{}/comments/{}/reactions'.format(
            channel_id, post_id, comment_id)
        params = dict_gen(emote_id=emote_value)
        return self._post(request, params=params)

    @oauth_required
    def delete_feed_comment_reaction(
            self,
            channel_id,
            post_id,
            comment_id,
            emote_value):
        request = 'feed/{}/posts/{}/comments/{}/reactions'.format(
            channel_id, post_id, comment_id)
        params = dict_gen(emote_id=emote_value)
        return self._delete(request, params=params)
