---
layout: page
title: windows/sfc (中文)
description: "扫描 Windows 系统文件的完整性。"
content_hash: fd400f204f45d2e004dfa676ff48b56a39cb2fa0
related_topics:
  - title: English version
    url: /en/windows/sfc.html
    icon: bi bi-globe
---
# sfc

扫描 Windows 系统文件的完整性。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- 显示命令的使用方法：

`sfc`

- 扫描所有的系统文件，如果可能的话，修复所有出现的问题：

`sfc /scannow`

- 扫描系统文件，但不修复出现的问题：

`sfc /verifyonly`

- 扫描指定的文件，如果可能的话，修复所有出现的问题：

`sfc /scanfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>

- 扫描指定的文件，但不修复出现的问题：

`sfc /verifyfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>

- 当离线修复时，指定引导目录：

`sfc /offbootdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

- 当离线修复时，指定 Windows 目录：

`sfc /offwindir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>
