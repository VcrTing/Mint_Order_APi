from rest_framework.versioning import URLPathVersioning

class MintVersioning(URLPathVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'