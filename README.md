# Azure Web App Configuration General Settings

Startup Command: gunicorn --bind 0.0.0.0 --worker-class aiohttp.worker.GunicornWebWorker  app:app

# Python Configuration

In [bot.py](dinspire/bot.py):

- Set `openai.api_key` to OpenAI's API key.
- Set `Ocp-Apim-Subscription-Key` to Azure Cognitive Service key from Keys and Endpoint.

In [config.py](dinspire/config.py):

- Set Azure Bot App ID in Configuration after `MicrosoftAppId`.
- Set Value in Azure Bot App ID Manage Password after `MicrosoftAppPassword`.
