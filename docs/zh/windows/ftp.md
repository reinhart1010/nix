---
layout: page
title: windows/ftp (中文)
description: "在本地和远程 FTP 服务器之间交互式传输文件。"
content_hash: 1a0ed99fb6b7cf017783a2a5c14788468f6227ee
related_topics:
  - title: English version
    url: /en/windows/ftp.html
    icon: bi bi-globe
---
# ftp

在本地和远程 FTP 服务器之间交互式传输文件。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/ftp>.

- 交互式连接一个远程的 FTP 服务：

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 匿名登录：

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 初始连接时禁用自动登录：

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 运行包含 FTP 命令列表的文件：

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 下载多个文件（通配符表达式）：

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- 上传多个文件（通配符表达式）：

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- 在远程服务器上删除多个文件：

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- 显示详细的帮助：

`ftp --help`
