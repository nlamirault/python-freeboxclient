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

import json
import logging
from os import path

import yaml

import freeboxclient
from freeboxclient import common

logger = logging.getLogger(__name__)


def get_configuration_filename():
    return "%s/.config/%s" % (path.expanduser("~"),
                              freeboxclient.CONFIG_FILE)


def load_configuration():
    config = get_configuration_filename()
    if path.exists(config):
        f = open(config)
        return yaml.load(f)
    else:
        raise common.FreeboxOSException("Configuration file not found : %s" %
                                        config)


def save_configuration(conf):
    config = get_configuration_filename()
    logger.debug("Save configuration : %s %s" % (conf, config))
    with open(config, 'wb') as yaml_file:
        json.dump(conf, yaml_file)
