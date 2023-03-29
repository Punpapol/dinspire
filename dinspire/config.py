#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "Azure Bot App ID in Configuration")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Value in Azure Bot App ID Manage Password")
