import json


class AbstractChangelog:

  def description(self) -> str:
    pass

  def transform_request(self, request):
    pass

  def transform_response(self, response):
    pass


class Changelog20210415(AbstractChangelog):

  def description(self):
    return "Changelog 2021-04-15: Add isRemediated to Threat Model"

  def transform_request(self, request):
    print(self.description(),"request")
    return request

  def transform_response(self, response):
    print(self.description(), "response")
    js = json.loads(response.getvalue())
    for e in js:
      e.pop('isRemediated', None)
    print(js)
    response.content = json.dumps(js)
    return response


class Changelog20210416(AbstractChangelog):

  def description(self):
    return "Changelog 2021-04-16: removed email from Threat Model"

  def transform_request(self, request):
    print(self.description(),"request")
    return request

  def transform_response(self, response):
    print(self.description(),"response")
    return response


class Changelog20210417(AbstractChangelog):

  def description(self):
    return "Changelog 2021-04-17: Add isRemediated to Threat Model"

  def transform_request(self, request):
    print(self.description(),"request")
    return request

  def transform_response(self, response):
    print(self.description(),"response")
    return response


LATEST_VERSION = "2021-04-17"

# latest version at the top
ALL_VERSIONS_CHANGELOG = [
  ("2021-04-17", [Changelog20210417()]),
  ("2021-04-16", [Changelog20210416()]),
  ("2021-04-15", [Changelog20210415()])
]


def get_latest_version():
  return LATEST_VERSION

def get_changelogs(version):
  ans = []
  for v in ALL_VERSIONS_CHANGELOG:
    if v[0] > version:
      ans += v[1]
  return ans

