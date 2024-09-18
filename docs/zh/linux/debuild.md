---
layout: page
title: linux/debuild (中文)
description: "从源代码构建 `Debian` 软件包的工具。"
content_hash: 6a1fd1ef645561b70398dc8b03702376acdc6b3f
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/debuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debuild

从源代码构建 `Debian` 软件包的工具。
更多信息：<https://manned.org/debuild.1>.

- 在当前目录中生成软件包：

`debuild`

- 仅构建二进制包：

`debuild -b`

- 生成软件包后，不运行 `lintian`（检查常见打包错误）：

`debuild --no-lintian`
