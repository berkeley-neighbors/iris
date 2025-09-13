import logging
import requests
from iris import db
from os import environ

logger = logging.getLogger(__name__)

class Authenticator:
    def __init__(self, config):
        self.config = config

    def authenticate(self, req):
        logger.info(f'Authenticating with Synology SSO')
        session = req.env['beaker.session']
        access_token = session.get('accessToken')
        
        if not access_token:
            return False

        SYNOLOGY_APP_ID = environ.get('SYNOLOGY_APP_ID')
        SYNOLOGY_OAUTH_URL = environ.get('SYNOLOGY_OAUTH_URL')
        sso_validate_url = SYNOLOGY_OAUTH_URL + '/webman/sso/SSOAccessToken.cgi'
        logger.debug(f'App ID: {SYNOLOGY_APP_ID}')
        
        params = {
            'action': 'exchange',
            'access_token': access_token,
            'app_id': SYNOLOGY_APP_ID
        }
        resp = requests.get(sso_validate_url, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data.get('success'):
            logger.error('Synology SSO token validation failed: %s', data)
            return False
        
        user_name = data.get('data', {}).get('user_name')
        print('username', user_name)
        if not user_name:
            return False

        conn = db.engine.raw_connection()
        cursor = conn.cursor(db.dict_cursor)
        cursor.execute('SELECT name FROM target WHERE name = %s AND `active` = TRUE', (user_name,))
        exists = cursor.fetchone()

        cursor.close()
        conn.close()
        
        if not exists:
            return False

        return user_name

SSO = True