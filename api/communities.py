from api.base import TwitchBase
from api.other.decorators import oauth_required
from api.other.helper import dict_gen
from api.other.constants import *


class Communities(TwitchBase):
    def get_community_by_name(self, community_name):
        request = 'communities'
        params = dict_gen(name=community_name)
        return self._get(request, params=params)

    def get_community_by_id(self, community_id):
        request = 'communities/{}'.format(community_id)
        return self._get(request)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def update_community(self, community_id, summary=None, description=None, rules=None, email=None):
        request = 'communities/{}'.format(community_id)
        json = dict_gen(summary=summary, description=description, rules=rules, email=email)
        return self._put(request, json=json)

    def get_top_communities(self, limit=10, cursor=None):
        request = 'communities/top'
        params = dict_gen(limit=limit, cursor=cursor)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_COMMUNITIES_MODERATE)
    def get_community_banned_users(self, community_id, limit=10, cursor=None):
        request = 'communities/{}/bans'.format(community_id)
        params = dict_gen(limit=limit, cursor=cursor)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_COMMUNITIES_MODERATE)
    def ban_community_user(self, community_id, user_id):
        request = 'communities/{}/bans/{}'.format(community_id, user_id)
        return self._get(request)

    @oauth_required(scope=SCOPE_COMMUNITIES_MODERATE)
    def un_ban_community_user(self, community_id, user_id):
        request = 'communities/{}/bans/{}'.format(community_id, user_id)
        return self._delete(request)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def create_community_avatar(self, community_id, avatar_image):
        request = 'communities/{}/images/avatar'.format(community_id)
        json = dict_gen(avatar_image=avatar_image)
        return self._post(request, json=json)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def delete_community_avatar(self, community_id):
        request = 'communities/{}/images/avatar'.format(community_id)
        return self._delete(request)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def create_community_cover_image(self, community_id, cover_image):
        request = 'communities/{}/images/cover'.format(community_id)
        json = dict_gen(cover_image=cover_image)
        return self._post(request, json=json)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def delete_community_cover_image(self, community_id):
        request = 'communities/{}/images/cover'.format(community_id)
        return self._delete(request)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def add_community_moderator(self, community_id, user_id):
        request = 'communities/{}/moderators/{}'.format(community_id, user_id)
        return self._put(request)

    @oauth_required(scope=SCOPE_COMMUNITIES_EDIT)
    def delete_community_moderator(self, community_id, user_id):
        request = 'communities/{}/moderators/{}'.format(community_id, user_id)
        return self._delete(request)

    @oauth_required
    def get_community_permissions(self, community_id):
        request = 'communities/{}/permissions'.format(community_id)
        return self._get(request)

    def report_community_violation(self, community_id, channel_id):
        request = 'communities/{}/report_channel'.format(community_id)
        json = dict_gen(channel_id=channel_id)
        return self._post(request, json=json)

    @oauth_required(scope=SCOPE_COMMUNITIES_MODERATE)
    def get_community_timed_out_users(self, community_id, limit=10, cursor=None):
        request = 'communities/{}/timeouts'.format(community_id)
        params = dict_gen(limit=limit, cursor=cursor)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_COMMUNITIES_MODERATE)
    def time_out_community_user(self, community_id, user_id, duration, reason=None):
        request = 'communities/{}/timeouts/{}'.format(community_id, user_id)
        json = dict_gen(duration=duration, reason=reason)
        return self._put(request, json=json)

    @oauth_required(scope=SCOPE_COMMUNITIES_MODERATE)
    def un_time_out_community_user(self, community_id, user_id):
        request = 'communities/{}/timeouts/{}'.format(community_id, user_id)
        return self._delete(request)
