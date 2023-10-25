---
layout: page
title: windows/sc (English)
description: "Communicate with the Service Control Manager and services."
content_hash: b789d5617a015c2ebee6995424a650ac9bbc1a12
last_modified_at: 2023-10-25
---
# sc

Communicate with the Service Control Manager and services.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Show the status of a service (no service name will list all services):

`sc.exe query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Start a service asynchronously:

`sc.exe create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` binpath= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\service_binary_file</span>

- Stop a service asynchronously:

`sc.exe delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Set the type of a service:

`sc.exe config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` type= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_type</span>
