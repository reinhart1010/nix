---
layout: page
title: windows/reg-export (English)
description: "Export the specified subkeys and values to a `.reg` file."
content_hash: 0a064a9ec7069c1fe79f4f4a5ef08572476c1121
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg export

Export the specified subkeys and values to a `.reg` file.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- Export all subkeys and values of a specific key:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.reg</span>

- Forcefully (assuming [y]es) overwrite of an existing file:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.reg</span>` /y`
