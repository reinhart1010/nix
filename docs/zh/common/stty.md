---
layout: page
title: common/stty (中文)
description: "设置终端设备接口的选项。"
content_hash: bf51d47cfa7fecc3064ca4024a30a8ef0fff8b4f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stty

设置终端设备接口的选项。
更多信息：<https://www.gnu.org/software/coreutils/stty>.

- 显示当前终端的所有设置：

`stty --all`

- 设置行数或列数：

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行数|列数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数量</span>

- 获取设备的实际传输速度：

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/驱动设备文件</span>` speed`

- 重置所有模式为当前终端的合理默认值：

`stty sane`
