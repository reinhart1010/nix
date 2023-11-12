---
layout: page
title: windows/reg-add (English)
description: "Add new keys and their values to the registry."
content_hash: ca168b735c210a2246555b93f6ba671395840210
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg add

Add new keys and their values to the registry.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

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
