---
layout: page
title: common/sv (中文)
description: "控制正在运行的服务。"
content_hash: 533b38fccf8c10717ccc5cb3a5d81412f8551cee
related_topics:
  - title: English version
    url: /en/common/sv.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sv

控制正在运行的服务。
更多信息：<https://manpages.ubuntu.com/manpages/latest/man8/sv.8.html>.

- 启动服务：

`sudo sv up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标目录 / 服务文件</span>

- 停止服务：

`sudo sv down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标目录 / 服务文件</span>

- 获取服务状态：

`sudo sv status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标目录 / 服务文件</span>
