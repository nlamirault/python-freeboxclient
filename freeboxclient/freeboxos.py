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


from cliff.app import App
from cliff.commandmanager import CommandManager
from freeboxclient.api import FreeboxClient
from freeboxclient.config import load_configuration
import logging
import sys


logger = logging.getLogger(__name__)


class FreeboxOSApp(App):

    log = logging.getLogger(__name__)
    freebox_client = None

    def __init__(self):
        super(FreeboxOSApp, self).__init__(
            description='freeboxos',
            version='0.1.0',
            command_manager=CommandManager('freeboxos'),
            )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')
        self.setup_freebox_client()

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)

    def setup_freebox_client(self):
        """ Creates a new client to the Freebox OS. """
        conf = load_configuration()
        self.log.info("Freebox configuration: %s" % conf)
        self.freebox_client = FreeboxClient(conf['app_id'],
                                            conf['app_name'],
                                            conf['app_version'],
                                            conf['device_name'])


def main(argv=sys.argv[1:]):
    app = FreeboxOSApp()
    return app.run(argv)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
