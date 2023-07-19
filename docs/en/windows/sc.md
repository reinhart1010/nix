---
layout: page
title: windows/sc (English)
description: "Communicate with the Service Control Manager and services."
content_hash: 4c69af2f2749c0feb8ba6ff65fa925176c74593b
last_modified_at: 2023-07-19
---
# sc

Communicate with the Service Control Manager and services.
More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query>.

- Show the status of a service (no service name will list all services):

`sc queryex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Start a service asynchronously:

`sc start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Stop a service asynchronously:

`sc stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Set the type of a service:

`sc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` type= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_type</span>
