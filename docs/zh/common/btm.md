---
layout: page
title: common/btm (中文)
description: "命令行`top`的替代品。"
content_hash: 945f589a7c97bb8364d43ceac230e0deff330c43
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/btm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/btm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btm

命令行`top`的替代品。
比 `top` 更轻便，支持跨平台、图表更丰富。
更多信息：<https://github.com/ClementTsang/bottom>.

- 展示默认布局（cpu, 内存，温度，磁盘，网络和 进程）：

`btm`

- 开启基础模式，关闭图表和高亮（接近于 `top`）：

`btm --basic`

- 将图表中的小点换成大点：

`btm --dot_marker`

- 展示电池充电和健康状态：

`btm --battery`

- 设置图表刷新间隔和留存数据的时长：

`btm --rate 250 --default_time_value 30000`
