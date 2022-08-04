---
layout: page
title: windows/reg-add (English)
description: "Add new keys and their values to the registry."
content_hash: 991315742d2d492f9da05d35ff7625fbe073751e
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-add.html
    icon: bi bi-globe
---
# reg add

Add new keys and their values to the registry.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- Add a new registry key:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Add a new value under a specific key:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Add a new value with specific data:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data</span>

- Add a new value to a key with a specific data type:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>

- Forcefully overwrite the existing registry value without a prompt:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /f`
