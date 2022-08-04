---
layout: page
title: common/aria2 (中文)
description: "一个轻量级多协议和多源命令行下载工具。"
content_hash: d942fe5747cc0b0391f9cf1f0708b98f583c5e19
related_topics:
  - title: bosanski version
    url: /bs/common/aria2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aria2.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aria2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aria2.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aria2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aria2

一个轻量级多协议和多源命令行下载工具。
支持 HTTP, HTTPS, FTP, SFTP, BitTorrent and Metalink.
主页： <https://aria2.github.io/>.

- 下载一个网络资源：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.iso</span>

- 从多个源处下载一个资源：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror1.org/myLinux.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror2.org/myLinux.iso</span>

- 使用两个连接下载资源：

`aria2c -x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.iso</span>

- 从 Metalink URI 中下载资源：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.metalink</span>

- 从 BitTorrent URI 中下载资源：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.torrent</span>

- 从 BitTorrent Magnet URI 中下载资源：

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'</span>

- 从一个文件中下载资源：

`aria2c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uris.txt</span>
