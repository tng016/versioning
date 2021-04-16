from .changelog import get_latest_version, get_changelogs

class VersioningMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    # One-time configuration and initialization.

  def __call__(self, request):
    # Code to be executed for each request before
    # the view (and later middleware) are called.
    self._inject_version_if_not_set(request)
    self.changelogs = get_changelogs(request.META["HTTP_VERSION"])
    request = self._transform_request(request)
    # print("request", request.META['HTTP_VERSION'])
    # print("body", request.body)
    # print("body", request.GET)
    # body_unicode = request.body.decode('utf-8')
    # print("newbodyunicode:", body_unicode)
    # body = json.loads(body_unicode)
    # print("newbody:", body)
    # print(request.path_info)
    # request.path_info = '/users/'

    response = self.get_response(request)

    # Code to be executed for each request/response after
    # the view is called.
    response = self._transform_response(response)

    return response

  def _inject_version_if_not_set(self, request):
    if "HTTP_VERSION" not in request.META:
      request.META["HTTP_VERSION"] = get_latest_version()

  def _transform_request(self, request):
    changelogs = self.changelogs
    for c in reversed(changelogs):
      request = c.transform_request(request)
    return request

  def _transform_response(self, response):
    changelogs = self.changelogs
    for c in changelogs:
      response = c.transform_response(response)
    return response