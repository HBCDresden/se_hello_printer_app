import unittest
import xml.etree.cElementTree as ET
from hello_world import app
from hello_world.formater import SUPPORTED

name = 'Krzysiu'
msg = 'Hello World!'


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in str(rv.data)

    def test_msg_with_output(self):
        name = 'Krzysiu'
        data_test = '{"imie": "' + name + '", "msg": "Hello World!"}'
        rv = self.app.get('/?output=json&name=' + name)
        self.assertEqual(data_test, rv.data)

    def test_message_with_xml_output(self):
        # <greetings>
        greetings = ET.Element("greetings")
        # <name>
        ET.SubElement(greetings, "name").text = name
        # <msg>
        ET.SubElement(greetings, "msg").text = msg
        xml = self.app.get('/?output=xml&name=' + name)
        self.assertEquals(ET.tostring(greetings), xml.data)
