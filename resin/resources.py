"""
This is a python library for resources like message templates etc.
"""


class Message(object):
    """
    Message templates
    """

    # Exception Error Message
    NOT_LOGGED_IN = "You have to log in!"
    UNAUTHORIZED = "You have to log in or RESIN_API_KEY environment variable must be set!"
    REQUEST_ERROR = "Request error: {body}"
    KEY_NOT_FOUND = "Key not found: {key}"
    DEVICE_NOT_FOUND = "Device not found: {uuid}"
    APPLICATION_NOT_FOUND = "Application not found: {application}"
    MALFORMED_TOKEN = "Malformed token: {token}"
    INVALID_DEVICE_TYPE = "Invalid device type: {dev_type}"
    INVALID_OPTION = "Invalid option: {option}"
    MISSING_OPTION = "Missing option: {option}"
    NON_ALLOWED_OPTION = "Non allowed option: {option}"
    LOGIN_FAILED = "Invalid credentials"
    DEVICE_OFFLINE = "Device is offline: {uuid}"
    DEVICE_NOT_WEB_ACCESSIBLE = "Device is not web accessible: {uuid}"
    INCOMPATIBLE_APPLICATION = "Incompatible application: {application}"
    INVALID_SETTINGS = "Settings file not found or not in proper format. Rewriting default settings to: {path}"
    SUPERVISOR_VERSION_ERROR = "Unsupported function! Supervisor version v{req_version} required, current supervisor version is v{cur_version}."
    AMBIGUOUS_APPLICATION = "Application is ambiguous: {application}"
    AMBIGUOUS_DEVICE = "Device is ambiguous: {uuid}"
    BUILD_NOT_FOUND = "Build not found: {id}"
    FAILED_BUILD = "Can not set to a failed build: {id}"
    INVALID_PARAMETER = "Invalid parameter: {value} is not a valid value for parameter `{parameter}`"
    IMAGE_NOT_FOUND = "Image not found: {id}"
