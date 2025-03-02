---
layout: page
title: linux/mknod (中文)
description: "创建块或字符设备特殊文件。"
content_hash: 5cd0b97992f041578f767af83fb1bd742fbc1139
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/mknod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mknod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mknod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mknod

创建块或字符设备特殊文件。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- 创建块设备：

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备文件</span>` b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主设备号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次设备号</span>

- 创建字符设备：

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备文件</span>` c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主设备号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次设备号</span>

- 创建先进先出（队列）设备：

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备文件</span>` p`

- 使用 SELinux 默认安全上下文创建设备文件：

`sudo mknod -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类型</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主设备号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次设备号</span>
