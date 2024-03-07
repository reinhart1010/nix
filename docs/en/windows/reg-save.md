---
layout: page
title: windows/reg-save (English)
description: "Save a registry key, its subkeys and values to a native `.hiv` file."
content_hash: 4f83208487efd1e1de9218263f98c8583d6ae243
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg save

Save a registry key, its subkeys and values to a native `.hiv` file.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- Save a registry key, its subkeys and values to a specific file:

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.hiv</span>

- Forcefully (assuming [y]es) overwrite an existing file:

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.hiv</span>` /y`
