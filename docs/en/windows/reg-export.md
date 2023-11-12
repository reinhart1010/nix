---
layout: page
title: windows/reg-export (English)
description: "Export the specified sub keys and values into a file."
content_hash: 1ddb34b6e9caadba1cff48963482e0d18523bc30
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg export

Export the specified sub keys and values into a file.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- Export all sub keys and values of a specific key:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.reg</span>

- Force overwriting of an existing file without prompt:

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.reg</span>` /y`
