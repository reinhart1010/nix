---
layout: page
title: common/zlib-flate (中文)
description: "原始 zlib 压缩和解压缩程序。"
content_hash: ca4989556ba3ac05b2c704a1798334333d129a7c
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zlib-flate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zlib-flate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zlib-flate

原始 zlib 压缩和解压缩程序。
`qpdf` 的一部分。
更多信息：<https://manned.org/zlib-flate>.

- 压缩一个文件：

`zlib-flate -compress < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入_文件</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩.zlib</span>

- 解压缩一个文件：

`zlib-flate -uncompress < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩.zlib</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出_文件</span>

- 使用指定的压缩级别压缩文件。0=最快（最差），9=最慢（最佳）：

`zlib-flate -compress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩级别</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入_文件</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩.zlib</span>
