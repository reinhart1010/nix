---
layout: page
title: common/airshare (中文)
description: "在本地网络中传输数据的工具。"
content_hash: caae922db29eaee40f0d3ff5116996154e6efe2c
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/common/airshare.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airshare.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airshare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airshare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airshare.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/airshare.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># airshare

在本地网络中传输数据的工具。
更多信息： <https://airshare.rtfd.io/en/latest/cli.html>.

- 共享文件或目录：

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录1 路径/到/文件或目录2 ...</span>

- 接收文件：

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- 主机接收服务器（使用此选项可以通过 Web 接口上传文件）：

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- 将文件或目录发送到接收服务器：

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录1 路径/到/文件或目录2 ...</span>

- 发送已复制到剪贴板的文件路径：

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- 接收文件并将其复制到剪贴板：

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>
