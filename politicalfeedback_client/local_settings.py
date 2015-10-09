import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BOWER_PATH = '/usr/local/bin/bower'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'carlotechnology'
EMAIL_HOST_PASSWORD = 'phoebe200196'

EMAIL_CLIENTE = 'carlo@fioretechnology.com'
EMAIL_MITT_CONTATTI = 'carlo@fioretechnology.com'

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE = True
PIPELINE_AUTO = True
PIPELINE_YUI_BINARY = '/usr/local/bin/yuicompressor'
