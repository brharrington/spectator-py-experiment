
import json
import sys
try:
    import urllib2
except ImportError:
    # python3 renames urllib2 to urllib.request
    import urllib.request as urllib2

class HttpClient:

    def post_json(self, uri, json):
        pass


class UrllibHttpClient(HttpClient):

    def __init__(self, registry):
        self._registry = registry

    def _add_status_tags(self, tags, code):
        tags["statusCode"] = "{}".format(code)
        tags["status"] = "{}xx".format(int(code / 100))

    def post_json(self, uri, data):
        headers = {
            "Content-Type": "application/json"
        }

        tags = {
            "client": "spectator-py",
            "method": "POST",
            "mode":   "http-client"
        }

        if type(data) is str:
            entity = data
        else:
            entity = json.dumps(data)
        request = urllib2.Request(uri, entity.encode('utf-8'), headers)

        start = self._registry.clock().monotonic_time()
        try:
            response = urllib2.urlopen(request)
            self._add_status_tags(tags, response.code)
        except urllib2.HTTPError as e:
            self._add_status_tags(tags, e.code)
        except urllib2.URLError as e:
            error = type(e).__name__
            tags["status"] = error
            tags["statusCode"] = error
        except:
            e = sys.exc_info()[0]
            error = type(e).__name__
            tags["status"] = error
            tags["statusCode"] = error

        duration = self._registry.clock().monotonic_time() - start
        self._registry.timer("http.req.complete", tags).record(duration)
