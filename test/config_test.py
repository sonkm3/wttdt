
import unittest
from lib.common.config import Config, get_status_handlers, get_reader, _klass_loader


class TestConfigFunctions(unittest.TestCase):
    def setUp(self):
        self.config = Config('test/config_test.yml')

    def test_config_handlers(self):
        handlers = get_status_handlers(self.config)

        self.assertEqual(self.config.status_handlers, self.config.status_handlers)
        self.assertEqual(handlers[1].arg1, self.config.status_handlers[1]['parameters']['arg1'])
        self.assertEqual(handlers[1].arg2, self.config.status_handlers[1]['parameters']['arg2'])

    def test_config_reader(self):
        reader = get_reader(self.config)

        self.assertEqual(reader.url, self.config.reader['parameters']['url'])

    def test_config_klass_loader(self):
        from testhandler import TestHandler
        test_handler1 = TestHandler()
        test_handler2 = _klass_loader('testhandler', 'TestHandler', {})

        self.assertEqual(test_handler1.__class__, test_handler2.__class__)


if __name__ == '__main__':
    unittest.main()



#PYTHONPATH=. python test/config_test.py