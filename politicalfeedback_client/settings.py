# Django settings for politicalfeedback project.
import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('zarloc', 'carlo@fioretechnology.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'politicalfeedback',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'politicalfeedback',
        'PASSWORD': 'testtest',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it-IT'

LOCALE_PATHS = (
    '/home/fiore/webapps/politicalfeedback/myproject/locale',
)


SITE_ID = 1

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/fiore/webapps/politicalfeedback/myproject/public/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://politicalfeedback.fioretechnology.com/public/cli/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/fiore/webapps/politicalfeedback/myproject/public/static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = 'http://politicalfeedback.fioretechnology.com/public/cli/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    '/home/fiore/webapps/politicalfeedback/myproject/static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# Make this unique, and don't share it with anybody.
SECRET_KEY = '$)a7n&o80u!6y5tdhs546!!shfdghpjpxc!ar&p#!)n1a'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',    
)

USE_ETAGS = True

ugettext = lambda s: s
LANGUAGES = (
             ('it', ugettext(u'Italiano')),
)

DEFAULT_LANGUAGE = 'it'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'it'


ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    '/home/fiore/webapps/politicalfeedback/myproject/templates',
)

INSTALLED_APPS = (

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'pipeline',
    'django.contrib.humanize',
    'haystack',
    'modeltranslation',
    # Uncomment the next line to enable the admin:
    'grappelli',
    'django.contrib.admin',
    'social_auth',
    #'accounts',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # debug dell'applicazione:
)

#facebook application
FACEBOOK_APP_ID = '759969377379292'
FACEBOOK_API_SECRET = 'd3f361b40ffa7b554155dfcd93575961'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_ERROR_URL    = '/login-error/'


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)


DEBUG_TOOLBAR_PATCH_SETTINGS = False

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.domain.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'tt'
EMAIL_HOST_PASSWORD = 'ff'

EMAIL_CLIENTE = 'carlo@fioretechnology.com'
EMAIL_MITT_CONTATTI = 'contatti@fioretechnology.com'


CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FONT_SIZE = 26
CAPTCHA_LETTER_ROTATION = (-10,10)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE = False
PIPELINE_AUTO = False
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_YUI_BINARY = '/home/fiore/webapps/politicalfeedback/bin/yuicompressor'
PIPELINE_YUI_CSS_ARGUMENTS = ''
PIPELINE_YUI_JS_ARGUMENTS = ''
PIPELINE_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_JS = {
    'base': {
        'source_filenames': (
          'js/base.js',
        ),
        'output_filename': 'js/base.min.js',
    }
}

PIPELINE_CSS = {
    'generic': {
        'source_filenames': (
          'css/screen.css',
        ),
        'output_filename': 'css/generic.min.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

THUMBNAIL_DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/fiore/memcached.sock',
        'TIMEOUT': 60000000000,
    }
}


#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#        'LOCATION': 'cachedb',
#    }
#}

THUMBNAIL_CACHE_TIMEOUT = None

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

GRAPPELLI_ADMIN_TITLE = "POLITICALFEEDBACK ADMIN"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

