---
layout: page
title: common/func (English)
description: "Azure Functions Core Tools: develop and test Azure Functions locally."
content_hash: 0bc752fc8eedce05be2cb0f4b917e06cee1db713
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# func

Azure Functions Core Tools: develop and test Azure Functions locally.
Local functions can connect to live Azure services, and can deploy a function app to an Azure subscription.
More information: <https://learn.microsoft.com/azure/azure-functions/functions-run-local>.

- Create a new functions project:

`func init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project</span>

- Create a new function:

`func new`

- Run functions locally:

`func start`

- Publish your code to a function app in Azure:

`func azure functionapp publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>

- Download all settings from an existing function app:

`func azure functionapp fetch-app-settings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>

- Get the connection string for a specific storage account:

`func azure storage fetch-connection-string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account</span>
