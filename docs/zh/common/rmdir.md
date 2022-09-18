---
layout: page
title: common/rmdir (中文)
description: "删除一个目录。"
content_hash: 8714c768834ff36ff5e7861d860afdc7568f4bcf
related_topics:
  - title: English version
    url: /en/common/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rmdir.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rmdir

删除一个目录。
更多信息：<https://www.gnu.org/software/coreutils/rmdir>.

- 删除空目录，使用 `rm -r` 删除非空目录：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 删除目标及其父目录（对嵌套的目录有用）：

`rmdir -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>
