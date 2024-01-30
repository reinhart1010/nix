---
layout: page
title: windows/systeminfo (English)
description: "Display operating system configuration for a local or remote machine."
content_hash: dea99258490de98c25b2412cb28c709bf0b18b95
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/windows/systeminfo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/systeminfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systeminfo

Display operating system configuration for a local or remote machine.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- Display system configuration for the local machine:

`systeminfo`

- Display system configuration in a specified output format:

`systeminfo /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Display system configuration for a remote machine:

`systeminfo /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Display help:

`systeminfo /?`
