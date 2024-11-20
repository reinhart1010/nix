---
layout: page
title: common/umount (中文)
description: "将文件系统与其挂载点解除链接，使其不再可访问。"
content_hash: a75bdc040b264af05495bcb84c1d7937ce662c08
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/umount.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/umount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# umount

将文件系统与其挂载点解除链接，使其不再可访问。
当文件系统正在使用时，无法卸载。
更多信息：<https://man.openbsd.org/umount>.

- 卸载文件系统，通过传递挂载源的路径：

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备文件</span>

- 卸载文件系统，通过传递挂载目标的路径：

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/挂载目录</span>

- 卸载所有已挂载的文件系统（`proc` 文件系统除外）：

`umount -a`
