---
layout: page
title: windows/reg-flags (English)
description: "Display or set flags on registry keys."
content_hash: 778823288549883bcdc839580bcbc65b0cab505f
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-flags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg flags

Display or set flags on registry keys.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-flags>.

- Display current flags for a specific key:

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` query`

- Set one or more flags, and unset unmentioned flags, for a specific key:

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flag_name1 flag_name2 ...</span>

- Set one or more flags for a specific key and its [s]ubkeys:

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flag_name1 flag_name2 ...</span>` /s`
