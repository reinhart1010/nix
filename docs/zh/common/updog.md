---
layout: page
title: common/updog (中文)
description: "Python {{SimpleHTTPServer}} 的替代方案。"
content_hash: 5bf347f963cfc1809bdf9fc8e040e1bdd628b7ca
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/updog.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/updog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/updog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># updog

Python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SimpleHTTPServer</span>` 的替代方案。
它允许通过 HTTP/S 上传和下载，可以设置临时 SSL 证书，并使用 HTTP 基本认证。
更多信息：<https://github.com/sc0tfree/updog>.

- 为当前目录启动 HTTP 服务器：

`updog`

- 为指定目录启动 HTTP 服务器：

`updog --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/目录</span>

- 在指定端口上启动 HTTP 服务器：

`updog --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>

- 使用密码启动 HTTP 服务器（要登录，请将用户名留空，并在密码字段中输入密码）：

`updog --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 通过 SSL 启用传输加密：

`updog --ssl`
