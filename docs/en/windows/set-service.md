---
layout: page
title: windows/set-service (English)
description: "Starts, stops, and suspends a service, and changes its properties."
content_hash: 9ac4233411221ea05108f20bafb44b8eafa8aace
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Set-Service

Starts, stops, and suspends a service, and changes its properties.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- Change a display name:

`Set-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -DisplayName "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Change the startup type of services:

`Set-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` -StartupType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Automatic</span>

- Change the description of a service:

`Set-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` -Description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`
