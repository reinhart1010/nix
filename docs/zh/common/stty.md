---
layout: page
title: common/stty (中文)
description: "设置终端设备接口的选项。"
content_hash: 28ee976bfebeced50300f26fe8cd760aac80347f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># stty

设置终端设备接口的选项。
更多信息：<https://www.gnu.org/software/coreutils/stty>.

- 显示当前终端的所有设置：

`stty -a`

- 设置行数：

`stty rows `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行数</span>

- 设置列数：

`stty cols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">列数</span>

- 获取设备的实际传输速度：

`stty -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标 / 文件夹 / 驱动设备文件</span>` speed`

- 将当前终端的所有模式重置为合理值：

`stty sane`
