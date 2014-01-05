#
# Copyright 2013 Nicolas Lamirault <nicolas.lamirault@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

import functools
import hashlib
import hmac
import json
import logging

import requests

from freeboxclient import common
from freeboxclient import config


logger = logging.getLogger(__name__)


class FreeboxClient():
    """Client for the FreeboxOS API.

    Attributes:
    - app_id: A unique app_id string
    - app_name: A descriptive application name displayed on lcd
    - app_version: the application version
    - device_name: The name of the device on which the app
    will be used
    """

    _url = 'http://mafreebox.freebox.fr'
    _version = 'api/v1'
    _fbx_header = 'X-Fbx-App-Auth'

    app_id = None
    app_name = None
    app_version = None
    device_name = None
    app_token = None
    track_id = None
    status = None
    challenge = None
    session_token = None
    api_version = None

    def __init__(self, conf):
        """Initialize a new client for the FreeboxOS API."""
        try:
            self.app_id = conf['app_id']
            self.app_name = conf['app_name']
            self.app_version = conf['app_version']
            self.device_name = conf['device_name']
        except KeyError as e:
            raise common.FreeboxOSException("Configuration error: %s" % e)
        # Registration parameters
        if 'app_token' in conf:
            self.app_token = conf['app_token']
        if 'track_id' in conf:
            self.track_id = conf['track_id']
        if 'status' in conf:
            self.status = conf['status']
        if 'challenge' in conf:
            self.challenge = conf['challenge']
        # Session
        if 'session_token' in conf:
            self.session_token = conf['session_token']

    def __str__(self):
        return "FreeboxOS(app_id=%s, app_name=%s, app_version=%s, "
        "device_name=%s, app_token=%s, track_id=%s, status=%s, "
        "challenge=%s)" % \
            (self.app_id, self.app_name, self.app_version, self.device_name,
             self.app_token, self.track_id, self.status, self.challenge)

    def _get_api_uri(self, request):
        """Make the HTTP uri to perform to retrieve information from
        the FreeboxOS.

        :param request: the REST uri
        """
        return '%s/%s/%s' % (self._url, self._version, request)

    def _get_valid_headers(self):
        """Make HTTP headers.

        :param session_token: a token for the current session
        """
        headers = {}
        headers['Content-type'] = 'application/json'
        headers['Accept'] = 'application/json'
        headers[self._fbx_header] = self.session_token
        logger.debug("[FreeboxOS] HTTP Headers: %s" % headers)
        return headers

    def _creates_password(self, app_token, challenge):
        """To authenticate the application, creates a password using a token
        and a challenge.

        :param app_token: token send by the FreeboxOS on the authorize request.
        :param challenge: a challenge send by the FreeboxOS.
        """
        if app_token is None or challenge is None:
            raise common.FreeboxOSException("Auth invalid: %s %s" %
                                            (app_token, challenge))
        else:
            logger.debug("Creates password: %s %s" % (app_token, challenge))
            return hmac.new(app_token, challenge, hashlib.sha1).hexdigest()

    def _freebox_get(self, uri):
        """Perform a HTTP GET request to the FreeboxOS.

        :param uri: the URL to call
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth
        """
        headers = self._get_valid_headers()
        logger.debug("[FreeboxOS] HTTP GET %s %s" % (uri, headers))
        response = requests.get(uri, headers=headers)
        logger.debug("[Freebox'] GET Response: %s %s" %
                     (response.status_code,
                      response.text))
        #return response
        if response.status_code == 200:
            content = response.json()
            if uri.endswith('api_version'):
                return content
            elif content['success'] is True:
                logger.debug("[FreeboxOS] Response JSON: %s" %
                             content['result'])
                return content['result']
            else:
                raise common.FreeboxOSException("Response error: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def _freebox_post(self, uri, params):
        """Perform a HTTP POST request to the FreeboxOS.

        :param uri: the URL to call
        :param params: a dict
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth
        """
        headers = self._get_valid_headers()
        logger.debug("[FreeboxOS] HTTP POST: %s %s %s" %
                     (uri, params, headers))
        response = requests.post(uri,
                                 headers=headers,
                                 data=json.dumps(params))
        logger.debug("[Freebox] POST Response: %s %s" %
                     (response.status_code,
                      response.text))
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                logger.debug("[FreeboxOS] Response JSON: %s" % content)
                if 'result' in content:
                    return content['result']
                else:
                    return content
            else:
                raise common.FreeboxOSException("Response error: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def _freebox_put(self, uri, params):
        """Perform a HTTP PUT request to the FreeboxOS.

        :param uri: the URL to call
        :param params: a dict
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth
        """
        headers = self._get_valid_headers()
        logger.debug("[FreeboxOS] HTTP PUT: %s %s %s" %
                     (uri, params, headers))
        response = requests.put(uri,
                                headers=headers,
                                data=json.dumps(params))
        logger.debug("[Freebox] PUT Response: %s %s" %
                     (response.status_code, response.text))
        return response

    def _freebox_delete(self, uri):
        """Perform a HTTP DELETE request to the FreeboxOS.

        :param uri: the URL to call
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth
        """
        headers = self._get_valid_headers()
        logger.debug("[FreeboxOS] HTTP DELETE: %s %s" %
                     (uri, headers))
        response = requests.delete(uri, headers=headers)
        logger.debug("[Freebox] DELETE Response: %s %s" %
                     (response.status_code, response.text))
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                logger.debug("[FreeboxOS] Response JSON: %s" % content)
                return content
            else:
                raise common.FreeboxOSException("Response error: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def to_dict(self):
        data = {}
        for attr in self.__dict__.keys():
            data[attr] = getattr(self, attr)
        return data

    def _need_authentication(self):
        if self.session_token is None:
            raise common.FreeboxOSAuthException("no session token found.")

    def authenticate(func):
        @functools.wraps(func)
        def wrapped(inst, *args, **kwargs):
            inst._need_authentication()
            return func(inst, *args, **kwargs)
        return wrapped

    #
    # API
    #

    def version(self):
        """Request to retrieve the Freebox OS api version."""
        uri = '%s/api_version' % self._url
        logger.debug("[Freebox] GET %s" % uri)
        return self._freebox_get(uri)

    def ask_authorization(self):
        """Request authorization to the Freebox OS."""
        params = {'app_id': self.app_id,
                  'app_name': self.app_name,
                  'app_version': self.app_version,
                  'device_name': self.device_name}
        uri = self._get_api_uri('login/authorize')
        content = self._freebox_post(uri, params)
        if 'track_id' in content and 'app_token' in content:
            self.track_id = content['track_id']
            self.app_token = content['app_token']
            logger.info("Accept this application. Look at the LCD screen.")
            config.save_configuration(self.to_dict())
        else:
            raise common.FreeboxOSException("Authorization failed: %s" %
                                            content)

    def check_authorization(self):
        """Request to retrieve authorization status from the Freebox OS."""
        if self.track_id:
            uri = self._get_api_uri('login/authorize/%s' % self.track_id)
            content = self._freebox_get(uri)
            if 'status' in content:
                self.status = content['status']
                self.challenge = content['challenge']
                config.save_configuration(self.to_dict())
                if self.status == 'granted':
                    logger.info("Application already granted on the "
                                "FreeboxOS.")
                    #authorized = True
                elif self.status == 'pending':
                    logger.info("Please confirmed the authorization request "
                                "on the FreeboxOS.")
                    #authorized = True
                elif self.status == 'unknown':
                    logger.info("Unknown application from the FreeboxOS. "
                                "Please send authorization again.")
                elif self.status == 'denied':
                    logger.info("This application has been denied by the "
                                "FreeboxOS.")
                elif self.status == 'timeout':
                    logger.info("Confirmation of the authorization has not "
                                "arrived on time.")
                return content
            else:
                raise common.FreeboxOSException("Authorization failed: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Please send authorization "
                                            "request before.")

    def login(self):
        """Make a request to the FreeboxOS to retrieve a challenge."""
        uri = self._get_api_uri('login')
        content = self._freebox_get(uri)
        if 'challenge' in content:
            self.challenge = content['challenge']
            logger.info("Freebox Login OK")
            config.save_configuration(self.to_dict())
        else:
            logger.info("Freebox Login KO")
            raise common.FreeboxOSException("Login failed: %s" % content)

    def open_session(self):
        """Request the FreeboxOS to retrieve a session token."""
        uri = self._get_api_uri('login/session')
        params = {'app_id': self.app_id,
                  'password': self._creates_password(self.app_token,
                                                     self.challenge)}
        content = self._freebox_post(uri, params)
        if 'session_token' in content:
            self.session_token = content['session_token']
            self.challenge = content['challenge']
            logger.info("Freebox Session opened.")
            config.save_configuration(self.to_dict())
        else:
            raise common.FreeboxOSException("Open session failed: %s" %
                                            content)

    def close_session(self):
        """Request to the FreeboxOS to close the current session."""
        uri = self._get_api_uri('login/logout')
        params = {'app_id': self.app_id,
                  'password': self._creates_password(self.app_token,
                                                     self.challenge)}
        content = self._freebox_post(uri, params)
        if 'success' in content:
            self.session_token = ''
            self.challenge = ''
            logger.info("Freebox Session closed.")
            config.save_configuration(self.to_dict())
        else:
            raise common.FreeboxOSException("Close session failed: %s" %
                                            content)

    # WIFI API

    @authenticate
    def get_wifi_status(self):
        """Request the FreeboxOS to retrive the WIFI status."""
        return self._freebox_get(self._get_api_uri('wifi'))

    @authenticate
    def get_wifi_config(self):
        """Request the FreeboxOS to retrive the WIFI configuration."""
        return self._freebox_get(self._get_api_uri('wifi/config'))

    @authenticate
    def reset_wifi_config(self):
        """Reset the Wifi configuration to the factory defaults."""
        return self._freebox_post(self._get_api_uri('wifi/config/reset'),
                                  {})

    @authenticate
    def get_wifi_stations(self, bss):
        """Get the list of Wifi stations associated to a BSS.

        :param bss: the Basic Service Set name
        """
        return self._freebox_get(self._get_api_uri('wifi/stations/%s' % bss))

    # CALLS API

    @authenticate
    def get_calls(self):
        """Returns the collection of alls."""
        return self._freebox_get(self._get_api_uri('call/log'))

    @authenticate
    def get_call(self, call_id):
        """Returns a call.

        :param call_id: the identifiant of the call
        """
        return self._freebox_get(self._get_api_uri('call/log/%s' % call_id))

    @authenticate
    def delete_call(self, call_id):
        """Delete a call.

        :param call_id: the identifiant of the call
        """
        return self._freebox_delete(self._get_api_uri('call/log/%s' %
                                                      call_id))
