---
layout: page
title: windows/wsl (中文)
description: "从命令行管理适用于 Linux 的 Windows 子系统。"
content_hash: 173daa5879dbcd48fd3a875100c8f19fd912777b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/wsl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wsl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/wsl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wsl

从命令行管理适用于 Linux 的 Windows 子系统。
更多信息：<https://learn.microsoft.com/windows/wsl/reference>.

- 启动 Linux Shell（在默认发行版中）：

`wsl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_命令</span>

- 在不使用 Shell 的情况下运行 Linux 命令：

`wsl --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令参数</span>

- 指定特定的发行版：

`wsl --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">发行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_命令</span>

- 列出所有可用发行版：

`wsl --list`

- 将发行版导出到 .tar 文件：

`wsl --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">发行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/distro_fs.tar</span>

- 从 .tar 文件导入发行版：

`wsl --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">发行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/安装位置</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/distro_fs.tar</span>

- 更改指定发行版的版本：

`wsl --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">发行版</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 关闭适用于 Linux 的 Windows 子系统：

`wsl --shutdown`
