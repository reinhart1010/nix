---
layout: page
title: windows/reg-restore (English)
description: "Restore a key and its values from a native `.hiv` file."
content_hash: 3e1c10318a275a300dafea44a1e953f145b5ff8a
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg restore

Restore a key and its values from a native `.hiv` file.
See `reg-save` for more information.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-restore>.

- Overwrite a specified key with data from a backup file:

`reg restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.hiv</span>
