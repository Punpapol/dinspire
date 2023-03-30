import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "Azure Bot App ID in Configuration")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Value in Azure Bot App ID Manage Password")
