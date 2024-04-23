---
layout: page
title: common/duf (中文)
description: "磁盘占用/空闲实用工具。"
content_hash: 523823e22a8d29f02bd539239c4899204d1f933f
last_modified_at: 2024-04-23
related_topics:
  - title: Deutsch version
    url: /de/common/duf.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/duf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duf

磁盘占用/空闲实用工具。
更多信息：<https://github.com/muesli/duf>.

- 列出可访问设备：

`duf`

- 列出所有（如伪文件系统，重复文件系统或不可访问的文件系统）：

`duf --all`

- 只显示指定的设备或挂载点：

`duf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件夹1 路径/到/文件夹2 ...</span>

- 根据指定条件排序输出：

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size|used|avail|usage</span>

- 显示或隐藏指定文件系统：

`duf --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">only-fs|hide-fs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs|vfat|ext4|xfs</span>

- 根据键排序输出：

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem</span>

- 更改主题（如果 `duf` 未能使用正确的主题）：

`duf --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|light</span>
