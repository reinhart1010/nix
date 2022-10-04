---
layout: page
title: windows/reg-save (English)
description: "Save a registry key, its sub keys and values to a file."
content_hash: 14f84e0af82d3e01bc7e92420dea0c6419315076
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-save.html
    icon: bi bi-globe
---
# reg save

Save a registry key, its sub keys and values to a file.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- Save a registry key, its sub keys and values to a specific file:

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Forcefully overwrite an existing file without a prompt:

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` /y`
