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

from freeboxclient import __version__
from freeboxclient.common import FreeboxOSException
import logging
import requests


logger = logging.getLogger(__name__)


class FreeboxClient():
    """ Client for the FreeboxOS API. """

    _url = 'http://mafreebox.freebox.fr'
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
        #To know if the APP is register on freeboxOS side
        self.registerIntoFreeboxServer = False
        #Registration parameters
        self.app_token = None
        self.track_id = None
        self.challenge = None

    def _get_api_uri(self, request):
        return '%s/%s' % (self._url, request)


    def _get_valid_headers(self):
        return {'Content-type': 'application/json',
                'Accept': 'application/json'}

    def _freebox_get(self, uri):
        return self.app.get(uri, headers=self._get_valid_headers())

    def _freebox_post(self, uri, params):
        return self.app.post(uri,
                             headers=self._get_valid_headers(),
                             data=json.dumps(params))

    def _freebox_put(self, uri, params):
        return self.app.put(uri,
                            headers=self._get_valid_headers(),
                            data=json.dumps(params))

    def _freebox_delete(self, uri):
        return self.app.delete(uri, headers=self._get_valid_headers())

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
        #uri = '%s/api_version' % self._url
        uri = self._get_api_uri('api_version')
        logger.info("[Freebox] GET %s" % uri)
        response = requests.get(uri)
        logger.info("[Freebox'] Response: %s %s" %
                    (response.status_code,
                     response.json()))
        if response.status_code == 200:
            return response.json()
        else:
            raise FreeboxOSException("Can't retrieve FreeboxOS version: %s" %
                                     response.text())

    def login(self):
        """ Request authorization to the Freebox OS. """
        params = {'app_id': self.app_id,
                  'app_name': self.app_name,
                  'app_version': self.app_version,
                  'device_name': self.device_name}
        uri = self._get_api_uri('login')
        response = requests.post(uri, data=json.dumps(params))
        logger.info("[Freebox'] Response: %s %s" %
                    (response.status_code,
                     response.json()))
