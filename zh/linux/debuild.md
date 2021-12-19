---
layout: page
title: linux/debuild (中文)
description: "从源代码构建 `Debian` 软件包的工具。"
content_hash: 9a86ebaaafa85e7bcda1469a3a4d426f34c8e123
related_topics:
  - title: English version
    url: /en/linux/debuild.html
    icon: bi bi-globe
---
# debuild

从源代码构建 `Debian` 软件包的工具。
更多信息：<https://manpages.debian.org/debuild>.

- 在当前目录中生成软件包：

`debuild`

- 仅构建二进制包：

`debuild -b`

- 生成软件包后，不运行 `lintian`（检查常见打包错误）：

`debuild --no-lintian`
