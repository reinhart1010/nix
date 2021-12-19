---
layout: page
title: windows/reg-delete (English)
description: "Delete keys or their values from the registry."
content_hash: eb7dc44b0d93f600ad8cf1d99b2a798cb0bc673d
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-delete.html
    icon: bi bi-globe
---
# reg delete

Delete keys or their values from the registry.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- Delete a specific registry key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Delete a value under a specific key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Delete all values recursively under the specified key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /va`

- Forcefully delete all values recursively under a key without a prompt:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /f /va`
