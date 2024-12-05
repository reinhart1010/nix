---
layout: page
title: common/zpool (中文)
description: "管理 ZFS 池。"
content_hash: 312f19cd4ed74e635d0c48ad3bef0693c9057798
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zpool.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zpool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zpool

管理 ZFS 池。
更多信息：<https://manned.org/zpool>.

- 显示所有 ZFS 池的配置和状态：

`zpool status`

- 检查 ZFS 池是否有错误（验证每个块的校验和）。非常消耗 CPU 和磁盘资源：

`zpool scrub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">池名称</span>

- 列出可导入的 ZFS 池：

`zpool import`

- 导入一个 ZFS 池：

`zpool import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">池名称</span>

- 导出一个 ZFS 池（卸载所有文件系统）：

`zpool export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">池名称</span>

- 显示所有池操作的历史记录：

`zpool history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">池名称</span>

- 创建一个镜像池：

`zpool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">池名称</span>` mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">磁盘1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">磁盘2</span>` mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">磁盘3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">磁盘4</span>

- 向 ZFS 池添加一个缓存（L2ARC）设备：

`zpool add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">池名称</span>` cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">缓存磁盘</span>
