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

from hashlib import sha1
import hmac
import json
import logging

import requests

from freeboxclient import common


logger = logging.getLogger(__name__)


class FreeboxClient():
    """Client for the FreeboxOS API."""

    _url = 'http://mafreebox.freebox.fr'
    _version = 'api/v1'
    _fbx_header = 'X-Fbx-App-Auth'
    api_version = None

    def __init__(self, app_id, app_name, app_version, device_name):
        """Initialize a new client for the FreeboxOS API.

        :param app_id: A unique app_id string
        :param app_name: A descriptive application name displayed on lcd
        :param app_version: the application version
        :param device_name: The name of the device on which the app
        will be used
        """
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.device_name = device_name
        # Registration parameters
        self.app_token = None
        self.track_id = None
        self.status = None
        self.challenge = None
        # Session
        self.session_token = None

    def _get_api_uri(self, request):
        """Make the HTTP uri to perform to retrieve information from
        the FreeboxOS.

        :param request: the REST uri"""
        return '%s/%s/%s' % (self._url, self._version, request)

    def _get_valid_headers(self, session_token=None):
        """Make HTTP headers.

        :param session_token: a token for the current session
        """
        headers = {}
        headers['Content-type'] = 'application/json'
        headers['Accept'] = 'application/json'
        if session_token:
            headers[self._fbx_header] = session_token
        return headers

    def _creates_password(self, app_token, challenge):
        """To authenticate the application, creates a password using a token
        and a challenge.

        :param app_token: token send by the FreeboxOS on the authorize request.
        :param challenge: a challenge send by the FreeboxOS.
        """
        return hmac.new(app_token, challenge, sha1).hexdigest()

    def _freebox_get(self, uri, session_token=None):
        """Perform a HTTP GET request to the FreeboxOS.

        :param uri: the URL to call
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth"""
        logger.info("[FreeboxOS] Get: %s" % uri)
        response = requests.get(uri,
                                headers=self._get_valid_headers())
        logger.info("[Freebox'] GET Response: %s %s" %
                    (response.status_code,
                     response.text))
        #return response
        if response.status_code == 200:
            content = response.json()
            if uri.endswith('api_version'):
                return content
            elif content['success'] is True:
                logger.info("[FreeboxOS] Response JSON: %s" %
                            content['result'])
                return content['result']
            else:
                raise common.FreeboxOSException("Response error: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def _freebox_post(self, uri, params, session_token=None):
        """Perform a HTTP POST request to the FreeboxOS.

        :param uri: the URL to call
        :param params: a dict
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth"""
        response = requests.post(uri,
                                 headers=self._get_valid_headers(),
                                 data=json.dumps(params))
        logger.info("[Freebox'] POST Response: %s %s" %
                    (response.status_code,
                     response.text))
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                logger.info("[FreeboxOS] Response JSON: %s" % content)
                return content
            else:
                raise common.FreeboxOSException("Response error: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def _freebox_put(self, uri, params, session_token=None):
        """Perform a HTTP PUT request to the FreeboxOS.

        :param uri: the URL to call
        :param params: a dict
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth"""
        response = requests.put(uri,
                                headers=self._get_valid_headers(),
                                data=json.dumps(params))
        logger.info("[Freebox'] PUT Response: %s %s" %
                    (response.status_code,
                     response.text))
        return response

    def _freebox_delete(self, uri, session_token=None):
        """Perform a HTTP DELETE request to the FreeboxOS.

        :param uri: the URL to call
        :param session_token: if session_token is not None,
        add it to the HTTP Header X-Fbx-App-Auth"""
        response = requests.delete(uri,
                                   headers=self._get_valid_headers())
        logger.info("[Freebox'] DELETE Response: %s %s" %
                    (response.status_code,
                     response.text))
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                logger.info("[FreeboxOS] Response JSON: %s" % content)
                return content
            else:
                raise common.FreeboxOSException("Response error: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    # def _saveRegistrationParams(self):
    #     """ Save registration parameters (app_id/token) to a local file """
    #     with open(self.registrationSaveFile, 'wb') as outfile:
    #         json.dump(self.registration, outfile)

    # def _loadRegistrationParams(self):
    #     if os.path.exists(self.registrationSaveFile):
    #         with open(self.registrationSaveFile) as infile:
    #             self.registration = json.load(infile)

    #
    # API
    #

    def version(self):
        """Request to retrieve the Freebox OS api version."""
        #uri = '%s/api_version' % self._url
        uri = '%s/api_version' % self._url
        logger.info("[Freebox] GET %s" % uri)
        return self._freebox_get(uri)

    def authorize(self):
        """Request authorization to the Freebox OS."""
        params = {'app_id': self.app_id,
                  'app_name': self.app_name,
                  'app_version': self.app_version,
                  'device_name': self.device_name}
        uri = self._get_api_uri('authorize')
        response = self._freebox_post(uri, params)
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                self.track_id = content['result']['track_id']
                self.app_token = content['result']['app_token']
                logger.info("Accept this application. Look at the LCD screen.")
            else:
                raise common.FreeboxOSException("Authorization failed: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request authorize failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def check_authorization(self, track_id):
        """Request to retrieve authorization status from the Freebox OS.

        :param track_id: the ID for the application
        """
        uri = self._get_api_uri('login/authorize/%s' % track_id)
        response = self._freebox_post(uri, {})
        #authorized = None
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                self.status = content['result']['status']
                self.challenge = content['result']['challenge']
                if self.status == 'granted':
                    logger.info("Application already granted on the FreeboxOS.")
                    #authorized = True
                elif self.status == 'pending':
                    logger.info("Please confirmed the authorization request on the FreeboxOS.")
                    #authorized = True
                elif self.status == 'unknown':
                    logger.info("This application is unknown from the FreeboxOS. Please send authorization again.")
                elif self.status == 'denied':
                    logger.info("This application has been denied by the FreeboxOS.")
                elif self.status == 'timeout':
                    logger.info("Confirmation of the authorization has not arrived on time.")
            else:
                raise common.FreeboxOSException("Authorization failed: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request check "
                                            "authorization failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def login(self):
        """Make a request to the FreeboxOS to retrieve a challenge."""
        uri = self._get_api_uri('login')
        response = self._freebox_get(uri)
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                self.challenge = content['result']['challenge']
            else:
                raise common.FreeboxOSException("Login failed: %s" % content)
        else:
            raise common.FreeboxOSException("Request login failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def open_session(self):
        """Request the FreeboxOS to retrieve a session token."""
        uri = self._get_api_uri('login/session')
        params = {'app_id': self.app_id,
                  'password': self._creates_password(self.app_token,
                                                     self.challenge)}
        response = self._freebox_post(uri, params)
        #authorized = None
        if response.status_code == 200:
            content = response.json()
            if content['success'] is True:
                self.session_token = content['result']['session_token']
                self.challenge = content['result']['challenge']
            else:
                raise common.FreeboxOSException("Open session failed: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request open session "
                                            "failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    def close_session(self):
        """ Request to the FreeboxOS to close the current session. """
        uri = self._get_api_uri('login/logout')
        response = self._freebox_post(uri, {})
        if response.status_code == 200:
            content = response.json()
            if content['success'] is not True:
                raise common.FreeboxOSException("Close session failed: %s" %
                                                content)
        else:
            raise common.FreeboxOSException("Request close "
                                            "session failed: %s %s" %
                                            (response.status_code,
                                             response.text))

    # WIFI API

    def get_wifi_status(self):
        """Request the FreeboxOS to retrive the WIFI status."""
        return self._freebox_get(self._get_api_uri('wifi'),
                                 self.session_token)

    def get_wifi_config(self):
        """Request the FreeboxOS to retrive the WIFI configuration."""
        return self._freebox_get(self._get_api_uri('wifi/config'),
                                 self.session_token)

    def reset_wifi_config(self):
        """Reset the Wifi configuration to the factory defaults."""
        return self._freebox_post(self._get_api_uri('wifi/config/reset'),
                                  {},
                                  self.session_token)

    def get_wifi_stations(self, bss):
        """Get the list of Wifi stations associated to a BSS.

        :param bss: the Basic Service Set name"""
        return self._freebox_get(self._get_api_uri('wifi/stations/%s' % bss),
                                 self.session_token)

    # CALLS API

    def get_calls(self):
        """Returns the collection of alls."""
        return self._freebox_get(self._get_api_uri('call/log'),
                                 self.session_token)

    def get_call(self, call_id):
        """Returns a call.

        :param call_id: the identifiant of the call
        """
        return self._freebox_get(self._get_api_uri('call/log/%s' % call_id),
                                 self.session_token)

    def delete_call(self, call_id):
        """Delete a call.

        :param call_id: the identifiant of the call
        """
        return self._freebox_delete(self._get_api_uri('call/log/%s' % call_id),
                                    self.session_token)
