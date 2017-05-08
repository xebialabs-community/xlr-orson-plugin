#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import requests

class OrsonClient(object):
    def __init__(self, orson_authentication):
        self.url = orson_authentication["url"]
        self.headers = {'Accept': 'application/json'}

    @staticmethod
    def get_client(orson_authentication):
        return OrsonClient(orson_authentication)

    def rest_request(self, api_url, method='GET', request_body=None, request_params=None):
        url = '{url}/{apiUrl}'.format(url=self.url, apiUrl=api_url)
        if (method == 'GET'):
            r = requests.get(
                url=url,
                verify=False,
                json=request_body,
                headers=self.headers,
                params=request_params,
            )
        elif (method == 'POST'):
            r = requests.post(
                url=url,
                verify=False,
                json=request_body,
            )
        return r.json()

    def orson_getdatadictionary(self, variables):
        data_dictionary = {}
        data_dictionary_datablock = self.rest_request("datablocks", "GET", None,  {"uniqueName":"data_dictionary_1.0"})
        return {'output' : data_dictionary}

    def orson_getscenarios(self, variables):
        scenarios = self.rest_request("scenarios", "GET", None, None)
        return {'output' : scenarios}

    def orson_getscenario(self, variables):
        scenario = self.rest_request("scenarios", "GET", None, {"uniqueName":variables['scenario_name']})
        return {'output' : scenario}



