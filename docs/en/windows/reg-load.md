---
layout: page
title: windows/reg-load (English)
description: "Load saved subkeys into a different subkey in the registry."
content_hash: d2c3b0ef6452b0a86a61fcea2c907bc0b7e7114b
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-load.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg load

Load saved subkeys into a different subkey in the registry.
Note: this is intended for troubleshooting and temporary keys.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-load>.

- Load a backup file into the specified key:

`reg load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.hiv</span>
