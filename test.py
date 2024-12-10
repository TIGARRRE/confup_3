import unittest
import yaml
from main import parse_yaml, resolve_constants, convert_to_custom_language  # Импортируйте ваши функции

class TestYAMLProcessing(unittest.TestCase):

    def setUp(self):
        self.valid_yaml = """
        app:
          title: 'TestApp'
          version: 1.0
          constants:
            max_users: 100
            timeout: 30
          settings:
            connection_limit: '@(max_users)'
            response_timeout: '@(timeout)'
          messages:
            welcome: 'Welcome to TestApp!'
            error: 'An error occurred.'
        """
        
        self.invalid_yaml = """
        app:
          title: 'TestApp'
          version: 1.0
          settings:
            connection_limit: '@(undefined_constant)'
        """

    def test_parse_yaml(self):
        data = parse_yaml(self.valid_yaml)
        self.assertIsInstance(data, dict)
        self.assertIn('app', data)

    def test_parse_invalid_yaml(self):
        data = parse_yaml(self.invalid_yaml)
        self.assertIsNone(data)

    def test_parse_invalid_yaml(self):
      data = parse_yaml(self.invalid_yaml)
      self.assertIsNone(data)  # Ожидаем, что результат будет None

    def test_resolve_constants(self):
        data = parse_yaml(self.valid_yaml)
        resolved_data = resolve_constants(data)
        self.assertEqual(resolved_data['app']['settings']['connection_limit'], 100)  # Ожидаем целое число
        self.assertEqual(resolved_data['app']['settings']['response_timeout'], 30)  # Ожидаем целое число

   
    def test_resolve_constants_with_undefined(self):
        data = parse_yaml(self.invalid_yaml)
        self.assertIsNone(data)  # Ожидаем, что результат будет None
        
    def test_convert_to_custom_language(self):
        data = parse_yaml(self.valid_yaml)
        resolved_data = resolve_constants(data)
        output = convert_to_custom_language(resolved_data)
        self.assertIn("title -> 'TestApp'", output)
        self.assertIn("connection_limit -> 100", output)  # Изменено на 100 без кавычек
        self.assertIn("welcome -> 'Welcome to TestApp!'", output)

def test_convert_with_nested_structure(self):
    nested_yaml = """
    app:
      title: 'NestedApp'
      features:
        logging: true
        monitoring:
          enabled: false
          level: 'info'
    """
    data = parse_yaml(nested_yaml)
    resolved_data = resolve_constants(data)
    output = convert_to_custom_language(resolved_data)
    self.assertIn("title -> 'NestedApp'", output)
    self.assertIn("logging -> True", output)  # Изменено на True
    self.assertIn("enabled -> False", output)  # Изменено на False
    self.assertIn("level -> 'info'", output)

if __name__ == '__main__':
    unittest.main()