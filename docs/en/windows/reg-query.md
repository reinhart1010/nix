---
layout: page
title: windows/reg-query (English)
description: "Display the values of keys and sub keys in the registry."
content_hash: f6e4cfa5383a889206f22b809810f24d439463d2
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg query

Display the values of keys and sub keys in the registry.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- Display all values of a key:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Display a specific value of a key:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Display all values of a key and its sub keys:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /s`

- Search for keys and values matching a specific pattern:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query_pattern</span>`"`

- Display a value of a key matching a specified data type:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>
