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
import sys

from cliff import app
from cliff import commandmanager

from freeboxclient import api
from freeboxclient import config


logger = logging.getLogger(__name__)


class FreeboxOSApp(app.App):

    log = logging.getLogger(__name__)
    freebox_client = None

    def __init__(self):
        super(FreeboxOSApp, self).__init__(
            description='freeboxos',
            version='0.1.0',
            command_manager=commandmanager.CommandManager('freeboxos'))

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
        """Creates a new client to the Freebox OS."""
        conf = config.load_configuration()
        self.log.debug("Freebox configuration: %s" % conf)
        self.freebox_client = api.FreeboxClient(conf)


def setup_logging():
    logging.basicConfig(format="%(asctime)s %(levelname)s - %(message)s",
                        filename='/tmp/freeboxos.log',
                        filemode='w',
                        level=logging.INFO)
    # hdlr = logging.FileHandler('/tmp/freeboxos.log')
    # formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    # hdlr.setFormatter(formatter)
    # logger.addHandler(hdlr)
    # logger.setLevel(logging.INFO)


def main(argv=sys.argv[1:]):
    setup_logging()
    app = FreeboxOSApp()
    return app.run(argv)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
