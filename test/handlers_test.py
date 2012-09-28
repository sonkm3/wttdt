import unittest
from lib.handler.echohandler import EchoHandler
from lib.handler.stophandler import StopHandler, StopException


class TestHandlersFunctions(unittest.TestCase):
    def setUp(self):
        self.message = 'abcdefg'
        self.blank_message = '   '

    def test_echo_handler(self):
        echo_handler = EchoHandler()
        self.assertEqual(echo_handler.handle(self.message), self.message)
        self.assertEqual(echo_handler.handle(self.blank_message), None)

    def test_stop_handler(self):
        stop_handler = StopHandler(1)

        def call_stop_handler():
            return stop_handler.handle(self.message)

        self.assertEqual(call_stop_handler(), self.message)
        self.assertRaises(StopException, call_stop_handler)


if __name__ == '__main__':
    unittest.main()



#PYTHONPATH=. python test/config_test.py