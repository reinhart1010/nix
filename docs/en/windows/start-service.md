---
layout: page
title: windows/start-service (English)
description: "Starts one or more stopped services."
content_hash: cb166e6724624366b754da9adbee585bbd474d74
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Start-Service

Starts one or more stopped services.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-service>.

- Start a service by using its name:

`Start-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Display information without starting a service:

`Start-Service -DisplayName *`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`* -WhatIf`

- Start a disabled service:

`Set-Service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` -StartupType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manual</span>`; Start-Service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
