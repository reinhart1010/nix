---
layout: page
title: windows/stop-service (English)
description: "Stops one or more running services."
content_hash: 2da6f6d9cc2ad979ab888cc21b45fa1729b44a14
last_modified_at: 2022-12-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Stop-Service

Stops one or more running services.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- Stop a service on the local computer:

`Stop-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Stop a service by using the display name:

`Stop-Service -DisplayName "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Stop a service that has dependent services:

`Stop-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` -Force -Confirm`
