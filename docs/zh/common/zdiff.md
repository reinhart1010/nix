---
layout: page
title: common/zdiff (中文)
description: "对 `gzip` 压缩文件调用 `diff`。"
content_hash: 1ae4272b56a14ed99f403905fb7763e186d88b49
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zdiff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zdiff

对 `gzip` 压缩文件调用 `diff`。
更多信息：<https://manned.org/zdiff>.

- 比较两个文件，必要时解压它们：

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2.gz</span>

- 将文件与同名的 `gzip` 压缩文件进行比较：

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
