---
layout: page
title: windows/reg-query (English)
description: "Display the values of keys and subkeys in the registry."
content_hash: 0214c99baddbb11fa372cb8c0659adb5ea655437
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg query

Display the values of keys and subkeys in the registry.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- Display all values of a key:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Display a specific [v]alue of a key:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Display all values of a key and its [s]ubkeys:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /s`

- Search [f]or keys and values matching a specific pattern:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query_pattern</span>`"`

- Display a value of a key matching a specified data [t]ype:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /t REG_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SZ|MULTI_SZ|EXPAND_SZ|DWORD|BINARY|NONE</span>

- Only search in [d]ata:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /d`

- Only search in [k]ey names:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /f /k`

- [c]ase-sensitively search for an [e]xact match:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /c /e`
