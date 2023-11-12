---
layout: page
title: windows/path (中文)
description: "显示或设置可执行文件的搜索路径。"
content_hash: bc779d1977bbce3d23af34d9ac3a8b24032aec6a
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/path.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/path.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/path.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/path.html
    icon: bi bi-globe
tldri18n_status: 2
---
# path

显示或设置可执行文件的搜索路径。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- 显示当前的路径：

`path`

- 将路径设置为一个或多个以分号分隔的目录：

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径 1[; 目录的路径 2]</span>

- 将新的目录添加到源路径后：

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>`;%path%`

- 将命令提示符设置为仅搜索当前目录中的可执行文件：

`path ;`
