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

import logging

from cliff import command


logger = logging.getLogger(__name__)


class FreeboxCommand(command.Command):
    """Default Freebox command."""

    pass


class FreeboxApiVersion(FreeboxCommand):
    """Retrieve the Freebox OS api version."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] API_Version")
        api_version = self.app.freebox_client.version()
        #print "Result: %s" % api_version
        self.app.stdout.write('FreeboxOS: %s\n' %
                              api_version['api_version'])


class FreeboxLogin(FreeboxCommand):
    """Login to the Freebox OS."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Login")
        self.app.freebox_client.login()
        self.app.stdout.write('FreeboxOS: %s\n' %
                              self.app.freebox_client)


class FreeboxAuthorize(FreeboxCommand):
    """Request authorization for this application."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Authorization request")
        self.app.freebox_client.ask_authorization()


class FreeboxCheckAuthorization(FreeboxCommand):
    """Request informations about authorization for this application."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Check Authorization ")
        self.app.freebox_client.check_authorization()


class FreeboxOpenSession(FreeboxCommand):
    """Open a new session to the FreeboxOS."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Open sesion")
        self.app.freebox_client.open_session()


class FreeboxCloseSession(FreeboxCommand):
    """Close the current session to the FreeboxOS."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Close sesion")
        self.app.freebox_client.close_session()


class FreeboxWifiStatus(FreeboxCommand):
    """Retrieve the WIFI status."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Wifi status")
        self.app.freebox_client.get_wifi_status()


class FreeboxWifiConfiguration(FreeboxCommand):
    """Retrieve the current WIFI configuration."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Wifi configuration")
        self.app.freebox_client.get_wifi_config()


class FreeboxWifiStations(FreeboxCommand):
    """Retrieve a list of wifi stations."""

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Wifi stations")
        self.app.freebox_client.get_wifi_stations()
