import pathlib

from newsroom.web.default_settings import CELERY_BEAT_SCHEDULE as CELERY_BEAT_SCHEDULE_DEFAULT


SERVER_PATH = pathlib.Path(__file__).resolve().parent
CLIENT_PATH = SERVER_PATH.parent.joinpath("client")

SITE_NAME = 'News Centre'
SHOW_USER_REGISTER = True
COPYRIGHT_HOLDER = 'LJI-IJL'
COPYRIGHT_NOTICE = ''
USAGE_TERMS = ''

PRIVACY_POLICY = PRIVACY_POLICY_EN = '/privacy'
TERMS_AND_CONDITIONS = TERMS_AND_CONDITIONS_EN = '/terms'
CONTACT_ADDRESS = 'https://www.thecanadianpress.com/contact/'
CONTACT_ADDRESS_EN = 'https://www.thecanadianpress.com/contact/'

WIRE_AGGS = {
    'service': {'terms': {'field': 'service.name', 'size': 50}},
    'subject': {'terms': {'field': 'subject.name', 'size': 20}},
}

WIRE_GROUPS = []

BLUEPRINTS = [
    'newsroom.wire',
    'newsroom.auth',
    'newsroom.users',
    'newsroom.companies',
    'newsroom.design',
    'newsroom.history',
    'newsroom.push',
    'newsroom.topics',
    'newsroom.upload',
    'newsroom.notifications',
    'newsroom.products',
    'newsroom.section_filters',
    'newsroom.navigations',
    'newsroom.cards',
    'newsroom.reports',
    'newsroom.public',
    'newsroom.settings',
    'newsroom.agenda',
]

CORE_APPS = [
    'superdesk.notification',
    'content_api.items',
    'content_api.items_versions',
    'content_api.search',
    'content_api.auth',
    'content_api.publish',
    'newsroom.users',
    'newsroom.companies',
    'newsroom.wire',
    'newsroom.topics',
    'newsroom.upload',
    'newsroom.history',
    'newsroom.ui_config',
    'newsroom.notifications',
    'newsroom.products',
    'newsroom.section_filters',
    'newsroom.navigations',
    'newsroom.cards',
    'newsroom.reports',
    'newsroom.public',
    'newsroom.settings',
    'newsroom.photos',
    'newsroom.media_utils',
    'newsroom.agenda',
]

COVERAGE_TYPES = {
    'text': {'name': 'Text', 'icon': 'text'},
    'photo': {'name': 'Photo', 'icon': 'photo'},
    'picture': {'name': 'Picture', 'icon': 'photo'},
    'audio': {'name': 'Audio', 'icon': 'audio'},
    'video': {'name': 'Video', 'icon': 'video'},
    'explainer': {'name': 'Explainer', 'icon': 'explainer'},
    'infographics': {'name': 'Infographics', 'icon': 'infographics'},
    'graphic': {'name': 'Graphic', 'icon': 'infographics'},
    'live_video': {'name': 'Live Video', 'icon': 'live-video'},
    'live_blog': {'name': 'Live Blog', 'icon': 'live-blog'},
    'video_explainer': {'name': 'Video Explainer', 'icon': 'explainer'}
}

DISPLAY_ABSTRACT = False

CLIENT_LOCALE_FORMATS = {
    "en": {  # defaults
        "TIME_FORMAT": "HH:mm",
        "DATE_FORMAT": "MMM DD, YYYY",
        "COVERAGE_DATE_TIME_FORMAT": "HH:mm DD/MM",
        "COVERAGE_DATE_FORMAT": "DD/MM",
    },
    "fr_CA": {
        "DATE_FORMAT": "DD MMM YYYY",
    }
}

LANGUAGES = ['en', 'fr_CA']
DEFAULT_LANGUAGE = 'en'

# Client configuration
CLIENT_CONFIG = {
    'default_language': DEFAULT_LANGUAGE,
    'locale_formats': CLIENT_LOCALE_FORMATS,
    'coverage_types': COVERAGE_TYPES,
    'display_abstract': DISPLAY_ABSTRACT,
    'list_animations': True,  # Enables or disables the animations for list item select boxes,
    'display_news_only': False,  # Displays news only switch in wire
    'item_actions': {
        'share': False,
    },
    'topic_actions': {
        'share': False,
    },
}

WATERMARK_IMAGE = None

CELERY_BEAT_SCHEDULE = {key: val for key, val in CELERY_BEAT_SCHEDULE_DEFAULT.items()
                        if key == 'newsroom.company_expiry'}

ENABLE_WATCH_LISTS = False

ACCOUNT_CREATED_EMAIL_SUBJECT = 'LJI News Centre account created/Accès au Centre de nouvelles de l’IJL'