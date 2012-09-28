# -*- coding: utf-8 -*-
import yaml

def _klass_loader(module_name, klass_name, arguments):
    module = __import__(module_name, [], [], [klass_name], 0)
    Klass = getattr(module, klass_name)
    return Klass(**arguments)

def get_reader(config):
    return _klass_loader(config.reader['module'], config.reader['class'], config.reader['parameters'])

def get_status_handlers(config):
    status_handler_list = []
    status_handlers = config.status_handlers

    for status_handler in status_handlers:
        module_name = status_handler['module']
        klass_name = status_handler['class']

        parameters = {}
        if 'parameters' in status_handler:
            parameters = status_handler['parameters']

        status_handler_list.append(_klass_loader(module_name, klass_name, parameters))

    return status_handler_list


class Config(object):
    def __init__(self, path_to_yaml):
        config = yaml.load(open(path_to_yaml).read())

        self.status_handlers = config['status_handlers']
        self.reader = config['reader']
