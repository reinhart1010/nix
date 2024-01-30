---
layout: page
title: windows/reg-flags (English)
description: "Display or set flags on registry keys."
content_hash: eacf959203c1681cc54888b33e1e49fe46b49880
last_modified_at: 2024-01-30
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

- Set specified space-separated flags, and unset unmentioned flags, for a specific key:

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flag_names</span>

- Set specified flags for a specific key and its sub keys:

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flag_names</span>` /s`

- Display help and available flag types:

`reg flags /?`
