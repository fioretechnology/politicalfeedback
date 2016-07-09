import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.abspath(__file__ + '/..'))

DEBUG = True

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
LANGUAGE_CODE = 'it_IT'

LOCALE_PATHS = (
	APP_ROOT +'/locale',
)


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
MEDIA_ROOT = APP_ROOT + '/public/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://staticpoliticalfeedback.fioretechnology.com/public/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = APP_ROOT + '/public/static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = 'http://staticpoliticalfeedback.fioretechnology.com/public/static/'

BOWERPATH = APP_ROOT + '/components/bower_components'

# Additional locations of static files
STATICFILES_DIRS = (
	APP_ROOT + "/static",
	BOWERPATH,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'djangobower.finders.BowerFinder',
	'compressor.finders.CompressorFinder',
	#'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = (
	"require.storage.OptimizedCachedStaticFilesStorage"
)



# Make this unique, and don't share it with anybody.
SECRET_KEY = '$)a7n&o80u!6y5t-+jrdgeshhrtjrwjhwwdsfjpxc!ar&p#!)n1a'


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
	'django.middleware.cache.FetchFromCacheMiddleware',
	'reversion.middleware.RevisionMiddleware',

)

USE_ETAGS = True

ugettext = lambda s: s
LANGUAGES = (
			 ('it', ugettext(u'Italiano')),
)

DEFAULT_LANGUAGE = 'it'


ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

BOWER_COMPONENTS_ROOT = APP_ROOT +'/components/'
BOWER_PATH = APP_ROOT + '/../bin/bower'
BOWER_INSTALLED_APPS = (
	'jquery',
	'foundation-sites',
	'foundation-datepicker',
	'requirejs',
	'datatables.net',
	'datatables.net-dt',
	'datatables.net-responsive',
	'datatables.net-responsive-dt',
	'datatables.net-buttons',
	'datatables.net-buttons-dt',
	'datatables.net-scroller',
	'datatables.net-scroller-dt',
	'datatables.net-select',
	'datatables.net-select-dt',
	'animate.css',
)

CKEDITOR_UPLOAD_PATH = "pagine/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"


TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [APP_ROOT + '/templates',],
		'OPTIONS': {
			'context_processors': [
				# Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
				# list if you haven't customized them:
				'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
				'django.contrib.messages.context_processors.messages',
			],
			'loaders': [
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
				'django.template.loaders.eggs.Loader',
			]
		},
	},
]

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'imagekit',
	'compressor',
	'django.contrib.humanize',
	'haystack',
	'django.contrib.admin',
	'djangobower',
	'reversion',
	'apps.accounts',
	'apps.pf',
	'ckeditor',
	'require',
)


REQUIRE_BASE_URL = "js"
REQUIRE_DEBUG = DEBUG
REQUIRE_JS = "../requirejs/require.js"
REQUIRE_EXCLUDE = ("grappelli/tinymce/jscripts/tiny_mce/themes/advanced/skins/grappelli/dialog.css",'grappelli/stylesheets/screen.css','css/jquery-ui-1.10.4.custom.css','css/entypo-icon.css','css/style/')



CKEDITOR_UPLOAD_PATH = "documenti/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': [
					['Bold', 'Italic', 'Underline'],
					['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
					['Undo', 'Redo', '-', 'RemoveFormat' ],
					["Link", "Unlink", "Anchor"],
					["Table", "HorizontalRule"],
					["Source"]
				],
		'language': 'it',
		'uiColor': '#dddddd',
		'height': 300,
		'width': "100%",
		'fontSize_defaultLabel': '14px',
	},
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'politicalfeedback'
EMAIL_HOST_PASSWORD = 'test'

EMAIL_CLIENTE = 'politicalfeedback@fioretechnology.com'
EMAIL_MITT_CONTATTI = 'politicalfeedback@fioretechnology.com'



CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FONT_SIZE = 26
CAPTCHA_LETTER_ROTATION = (-10,10)

COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (
	("text/x-scss", 'sass --scss'),
)


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

#filter settings
N_PERPAGINA = 24


GRAPPELLI_ADMIN_TITLE = "POLITICALFEEDBACK ADMIN"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
SERVER_EMAIL ='politicalfeedback@fioretechnology.com'

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

ANALYTICS_ID = 'aa'
SITO_SLUG = 'core' # Nome del sito per i file del dominio statico


try:
	from local_settings import *
except ImportError:
	pass
