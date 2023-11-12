---
layout: page
title: osx/mdutil (中文)
description: "管理 Spotlight（聚焦搜索）用于搜索的索引数据。"
content_hash: 0fef3c7b9c4ca7121df68806ec601ddff293edeb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/mdutil.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mdutil

管理 Spotlight（聚焦搜索）用于搜索的索引数据。
更多信息：<https://ss64.com/osx/mdutil.html>.

- 显示指定卷（'/'）的索引状态：

`mdutil -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- 打开 / 关闭给定卷的 Spotlight 索引：

`mdutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定卷文件夹</span>

- 清除索引数据并重新建立索引：

`mdutil -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定卷文件夹</span>
