# Webserver
from flask import Flask, make_response, Response
from flask_restx import Resource, Api, reqparse
import xml.etree.ElementTree as ET

# Instantiate flask app and corresponding REST Api
app = Flask(__name__)
api = Api(app)

@api.route('/xml_endpoint')
class XMLEndpoint(Resource):
    def get(self):
        # Parse arguments
        parser = reqparse.RequestParser()
        parser.add_argument('name1', type=str, help='groom')
        parser.add_argument('name2', type=str, help='bride')
        args = parser.parse_args()

        # Build response with flask function, default http code is 200 (OK)
        #response = make_response({"text": text})
        # Add header so Angular doesnt complain
        # response.headers.add("Access-Control-Allow-Origin", "*")
        #return response
        root = ET.Element('list_tag')
        for i in range(15):
            x = ET.SubElement(root, 'struct_tag', {'int_val': str(i), 'float_val': str(-3.5 + i),
                                                'string_val': "abc" if i % 2 == 0 else "def"})

        # response = make_response( {"str": rootStr})
        #return str(asBytes)
        return Response(ET.tostring(root, encoding="ascii", method="xml"), mimetype='text/xml')

# --------------------------------------------------------------------------

if __name__ == '__main__':
    # Host on 0.0.0.0 (all local adresses), as localhost (loopback) will not be routed through docker
    app.run(host = '127.0.0.1', port=8000, debug=False)
