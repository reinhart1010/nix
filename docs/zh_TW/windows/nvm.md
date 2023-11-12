---
layout: page
title: windows/nvm (中文 (繁體, 台灣))
description: "安裝、解除安裝，或切換不同 Node.js 版本。"
content_hash: f98a4beefb422ad62d936aa24e3d6376dbfbb0ef
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/nvm.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/nvm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/nvm.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nvm

安裝、解除安裝，或切換不同 Node.js 版本。
支援版本號如「12.8」或「v16.13.1」，以及像是「stable」、「system」等標籤。
更多資訊：<https://github.com/coreybutler/nvm-windows>.

- 安裝特定版本的 Node.js：

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node 版本</span>

- 設定系統預設使用的 Node.js 版本（必須以系統管理員身分執行）：

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node 版本</span>

- 列出所有已安裝的 Node.js 版本，並標註當前系統使用的版本：

`nvm list`

- 解除安裝指定的 Node.js 版本：

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node 版本</span>
