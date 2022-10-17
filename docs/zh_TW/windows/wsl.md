---
layout: page
title: windows/wsl (中文 (繁體, 台灣))
description: "透過命令行管理 Windows 子系統 Linux 版 (WSL)。"
content_hash: 4c56e98475bca71714b3f948c6acc73fb70d2a54
related_topics:
  - title: Deutsch version
    url: /de/windows/wsl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wsl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wsl

透過命令行管理 Windows 子系統 Linux 版 (WSL)。
更多資訊：<https://learn.microsoft.com/windows/wsl/reference>.

- 在預設發行版下，開啟 Linux shell：

`wsl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell 命令</span>

- 不使用 shell 執行 Linux 命令：

`wsl --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令參數</span>

- 指定發行版：

`wsl --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">發行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell 命令</span>

- 列出可用的發行版：

`wsl --list`

- 將發行版匯出至 `.tar` 檔：

`wsl --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">發行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/distro_fs.tar</span>

- 從 `.tar` 檔匯入發行版：

`wsl --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">發行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/安裝位置</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/distro_fs.tar</span>

- 變更執行特定發行版的 Windows 子系統 Linux 版本

`wsl --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">發行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">WSL 版本</span>

- 終止執行 Windows 子系統 Linux 版

`wsl --shutdown`
