import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in str(rv.data)

    def test_msg_with_output(self):
        name = 'Krzysiu'
        data_test = b'{ "imie":"' + name + '", "mgs":"Hello World!"}'
        rv = self.app.get('/?output=json&name=' + name)
        self.assertEqual(data_test, rv.data)

    def test_message_with_xml_output(self):
        name = 'Krzysiu'
        data_test = '<greetings><name>'+ name +' ' + '</name><msg>Hello World!</msg></greetings>'
        xml = self.app.get('/?output=xml&name=' + name)
        self.assertEqual(data_test, xml.data)
