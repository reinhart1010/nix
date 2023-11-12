---
layout: page
title: windows/iscc (中文)
description: "Inno Setup 安装程序的编译器。"
content_hash: 89bceb43ff83ae9509c294a5e00ef52d23135d6e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/iscc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iscc

Inno Setup 安装程序的编译器。
它将 Inno Setup 脚本编译为 Windows 安装程序可执行文件。
更多信息：<https://jrsoftware.org/isinfo.php>.

- 编译一个 Inno Setup 脚本：

`iscc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">脚本路径.iss</span>

- 静默编译一个 Inno Setup 安装程序：

`iscc /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">脚本路径.iss</span>

- 编译已签名的 Inno Setup 安装程序：

`iscc /S=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">脚本路径.iss</span>
