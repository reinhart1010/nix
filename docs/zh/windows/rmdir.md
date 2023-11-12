---
layout: page
title: windows/rmdir (中文)
description: "删除一个目录和其中的内容。"
content_hash: b57fd29256706985b955c18bea0490ee05b9b93b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rmdir

删除一个目录和其中的内容。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 删除一个空目录：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

- 递归删除一个目录及其中的内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>` /s`

- 在没有提示的情况下递归删除目录及其内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` /s /q`
