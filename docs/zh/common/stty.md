---
layout: page
title: common/stty (中文)
description: "设置终端设备接口的选项。"
content_hash: 8a194ae46a818d313178c6639f897fd1c0eb9218
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/stty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># stty

设置终端设备接口的选项。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- 显示当前终端的所有设置：

`stty --all`

- 设置行数或列数：

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行数|列数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数量</span>

- 获取设备的实际传输速度：

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/驱动设备文件</span>` speed`

- 重置所有模式为当前终端的合理默认值：

`stty sane`
