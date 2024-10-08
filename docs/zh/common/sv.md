---
layout: page
title: common/sv (中文)
description: "控制正在运行的服务。"
content_hash: 1655ce93f42b4b6375b7e741d706082a97a88f9f
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/sv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sv

控制正在运行的服务。
更多信息：<https://manned.org/sv.8>.

- 启动服务：

`sudo sv up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标目录 / 服务文件</span>

- 停止服务：

`sudo sv down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标目录 / 服务文件</span>

- 获取服务状态：

`sudo sv status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标目录 / 服务文件</span>
