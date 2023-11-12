---
layout: page
title: common/aria2c (中文)
description: "快速下载工具。"
content_hash: fcedc65d144b9c3503989fee033a4137519cf70e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aria2c.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aria2c.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aria2c.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aria2c.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aria2c.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aria2c.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aria2c

快速下载工具。
支持 HTTP(S), FTP, SFTP, BitTorrent, and Metalink.
更多信息：<https://aria2.github.io>.

- 下载一个 URI 到文件：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 从多个源处下载一个资源：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_2</span>

- 通过保存在一个文件中的 URL 列表来下载资源：

`aria2c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 使用多个连接下载资源：

`aria2c -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">连接数量</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 通过带用户名密码验证的 FTP 协议下载资源：

`aria2c --ftp-user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --ftp-passwd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 限制下载速度（bytes/s）：

`aria2c --max-download-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">速度</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
