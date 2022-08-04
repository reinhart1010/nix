---
layout: page
title: windows/reg-query (English)
description: "Display the values of keys and sub keys in the registry."
content_hash: 81e0605a3b06cbbd9f6122ae13f3e7a65843e7ff
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-query.html
    icon: bi bi-globe
---
# reg query

Display the values of keys and sub keys in the registry.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/reg-query>.

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
