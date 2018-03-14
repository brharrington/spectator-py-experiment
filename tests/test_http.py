#!/usr/bin/env python3

from netflix.spectator import Registry
from netflix.spectator.http import UrllibHttpClient

import json
import threading
import unittest

try:
    from BaseHTTPServer import HTTPServer
    from BaseHTTPServer import BaseHTTPRequestHandler
except ImportError:
    # python3
    from http.server import HTTPServer
    from http.server import BaseHTTPRequestHandler

class HttpTest(unittest.TestCase):

    def setUp(self):
        self._server = HTTPServer(("localhost", 0), TestHandler)
        self._uri = "http://localhost:{}/path".format(self._server.server_port)
        t = threading.Thread(target=self._server.serve_forever)
        t.start()

    def tearDown(self):
        self._server.shutdown()
        self._server.server_close()

    def test_do_post_ok(self):
        r = Registry()
        client = UrllibHttpClient(r)
        client.post_json(self._uri, '{"status": 200}')
        tags = {
            "mode":       "http-client",
            "method":     "POST",
            "client":     "spectator-py",
            "status":     "2xx",
            "statusCode": "200"
        }
        t = r.timer("http.req.complete", tags)
        self.assertEqual(t.count(), 1)

    def test_do_post_404(self):
        r = Registry()
        client = UrllibHttpClient(r)
        client.post_json(self._uri, '{"status": 404}')
        tags = {
            "mode":       "http-client",
            "method":     "POST",
            "client":     "spectator-py",
            "status":     "4xx",
            "statusCode": "404"
        }
        t = r.timer("http.req.complete", tags)
        self.assertEqual(t.count(), 1)

    def test_do_post_bad_json(self):
        r = Registry()
        client = UrllibHttpClient(r)
        client.post_json(self._uri, '{"status": ')
        tags = {
            "mode":       "http-client",
            "method":     "POST",
            "client":     "spectator-py",
            "status":     "4xx",
            "statusCode": "400"
        }
        t = r.timer("http.req.complete", tags)
        self.assertEqual(t.count(), 1)

    def test_do_post_encode(self):
        r = Registry()
        client = UrllibHttpClient(r)
        client.post_json(self._uri, {"status": 202})
        tags = {
            "mode":       "http-client",
            "method":     "POST",
            "client":     "spectator-py",
            "status":     "2xx",
            "statusCode": "202"
        }
        t = r.timer("http.req.complete", tags)
        self.assertEqual(t.count(), 1)

    def test_do_post_network_error(self):
        self.tearDown()
        r = Registry()
        client = UrllibHttpClient(r)
        client.post_json(self._uri, "{}")
        tags = {
            "mode":       "http-client",
            "method":     "POST",
            "client":     "spectator-py",
            "status":     "URLError",
            "statusCode": "URLError"
        }
        t = r.timer("http.req.complete", tags)
        self.assertEqual(t.count(), 1)

class TestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(length))
            self.send_response(data["status"])
            self.end_headers()
        except:
            self.send_response(400)
            self.end_headers()


if __name__ == '__main__':
    unittest.main()
