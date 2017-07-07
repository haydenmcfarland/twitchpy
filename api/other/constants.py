# TWITCH API V5
TWITCH_API_V5_ROOT = 'https://api.twitch.tv/kraken/'
TWITCH_API_V5_ACCEPT = 'application/vnd.twitchtv.v5+json'

# DIRECTION
DIRECTION_ASC = 'asc'
DIRECTION_DESC = 'desc'
VALID_DIRECTIONS = [DIRECTION_ASC, DIRECTION_DESC]

# OBJECT LIMITS
MAX_OBJECT_LIMIT = 100
DEFAULT_OBJECT_LIMIT = 25
DEFAULT_VIDEO_LIMIT = 10
DEFAULT_OFFSET = 0

# BROADCAST
BROADCAST_TYPES = ['archive', 'highlight', 'upload']
DEFAULT_BROADCAST = ','.join(BROADCAST_TYPES)

# LANGUAGE
LANGUAGES = ['en', 'es']
DEFAULT_LANGUAGES = ','.join(LANGUAGES)

# SORT
SORT_TYPES = ['views', 'time']
DEFAULT_SORT = 'time'

# SCOPE CHANNEL_FEED
SCOPE_CHANNEL_FEED_EDIT = 'channel_feed_edit'

# SCOPE CHANNEL
SCOPE_CHANNEL_READ = 'channel_read'
SCOPE_CHANNEL_SUBSCRIPTIONS = 'channel_subscriptions'
SCOPE_CHANNEL_CHECK_SUBSCRIPTION = 'channel_check_subscription'
SCOPE_CHANNEL_EDITOR = 'channel_editor'
SCOPE_CHANNEL_COMMERCIAL = 'channel_commercial'
SCOPE_CHANNEL_STREAM = 'channel_stream'

# SCOPE COLLECTIONS
SCOPE_COLLECTIONS_EDIT = 'collections_edit'

# SCOPE COMMUNITIES
SCOPE_COMMUNITIES_EDIT = 'communities_edit'
SCOPE_COMMUNITIES_MODERATE = 'communities_moderate'

# SCOPE USER
SCOPE_USER_READ = 'user_read'
SCOPE_USER_SUBSCRIPTIONS = 'user_subscriptions'
SCOPE_USER_FOLLOWS_EDIT = 'user_follows_edit'
SCOPE_USER_BLOCKS_READ = 'user_blocks_read'
SCOPE_USER_BLOCKS_EDIT = 'user_blocks_edit'

# SCOPE VHS
SCOPE_VIEWING_ACTIVITY_READ = 'viewing_activity_read'

# TWITCH BASE REQUESTS
PUT = 'put'
POST = 'post'
GET = 'get'
DELETE = 'delete'
