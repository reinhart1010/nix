---
layout: page
title: windows/logoff (中文 (繁體, 台灣))
description: "終止登入的工作階段。"
content_hash: 57ba8a0d8e5a86c723a5631f5ad7b9d12190c8b3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/logoff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/logoff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/logoff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logoff

終止登入的工作階段。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- 終止當前工作階段：

`logoff`

- 通過名稱和 ID 終止工作階段：

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">工作階段名稱|工作階段 ID</span>

- 終止通過 RDP 連接到指定伺服器的工作階段：

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">工作階段名稱|工作階段 ID</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">伺服器</span>
