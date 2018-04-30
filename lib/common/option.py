# -*- coding: utf-8 -*-
from optparse import OptionParser


def get_option():

    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config_yaml", help="config file(yaml)", metavar="CONFIG_YAML")

    (options, args) = parser.parse_args()

    return options
