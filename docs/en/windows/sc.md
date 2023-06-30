---
layout: page
title: windows/sc (English)
description: "Communicate with the Service Control Manager and services."
content_hash: cd7325b8d4aee7d3ca5b1c922e8faead69a2a627
last_modified_at: 2023-06-30
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sc

Communicate with the Service Control Manager and services.
More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query>.

- Show the status of a service:

`sc queryex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Start a service asynchronously:

`sc start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Stop a service asynchronously:

`sc stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Set the type of a service:

`sc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` type= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_type</span>
