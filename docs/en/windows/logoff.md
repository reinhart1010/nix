---
layout: page
title: windows/logoff (English)
description: "Terminate a login session."
content_hash: 7b89883743861f66dc7cd1e82e2caefebb16f0cc
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/windows/logoff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/logoff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logoff

Terminate a login session.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- Terminate the current session:

`logoff`

- Terminate a session by its name or id:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name|session_id</span>

- Terminate a session on a specific server connected through RDP:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name|session_id</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servername</span>
