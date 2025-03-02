---
layout: page
title: common/jmtpfs (中文)
description: "基于 FUSE 的文件系统，用于访问 MTP 设备。"
content_hash: fbd091364b564fa4366da6648ed8434c66946f9f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jmtpfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jmtpfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jmtpfs

基于 FUSE 的文件系统，用于访问 MTP 设备。
更多信息：<https://manned.org/jmtpfs>.

- 将一个 MTP 设备挂载到一个目录：

`jmtpfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 设置挂载选项：

`jmtpfs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">allow_other,auto_unmount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 列出可用的 MTP 设备：

`jmtpfs --listDevices`

- 如果存在多个设备，挂载一个特定的设备：

`jmtpfs -device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">总线_id</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">设备_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 卸载 MTP 设备：

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>
