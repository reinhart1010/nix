---
layout: page
title: common/zdb (中文)
description: "ZFS 调试器。"
content_hash: cd693660d38ad12382bd26f5b89cd1cf21a9e5b2
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zdb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zdb

ZFS 调试器。
更多信息：<https://manned.org/zdb>.

- 显示所有已挂载 ZFS 存储池的详细配置：

`zdb`

- 显示特定 ZFS 存储池的详细配置：

`zdb -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称</span>

- 显示关于块的数量、大小和重复数据删除的统计信息：

`zdb -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称</span>
