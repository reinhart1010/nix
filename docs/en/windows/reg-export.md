---
layout: page
title: windows/reg-export (English)
description: "Export the specified sub keys and values into a file."
content_hash: 202af3881c3f38ac0307f2fdf925e20d515f3f47
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-export.html
    icon: bi bi-globe
---
# reg export

Export the specified sub keys and values into a file.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- Export all sub keys and values of a specific key:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.reg</span>

- Force overwriting of an existing file without prompt:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.reg</span>` /y`
