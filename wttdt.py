# -*- coding: utf-8 -*-

import signal
from lib.common.config import Config
from lib.common.wttdtcontroller import WttdtController
from lib.common.errorhandler import ErrorHandler
from lib.common.signalhandler import SignalHandler
from lib.common.option import get_option

from lib.common.shutdownhandler import ShutdownHandler


def main():
    shutdown_handler = None

    option = get_option()

    signal_handler = SignalHandler()
    signal.signal(signal.SIGINT, signal_handler.handle)

    try:
        config = Config(option.config_yaml)

        wttdt_controller = WttdtController(config)

        shutdown_handler = ShutdownHandler(wttdt_controller.status_handlers)

        wttdt_generator = wttdt_controller.run()
        for wttdt_status in wttdt_generator:
            result = wttdt_status

    except:
        ErrorHandler.handle()

    finally:
        if shutdown_handler:
            shutdown_handler.shutdown()

if __name__ == '__main__':
    main()
