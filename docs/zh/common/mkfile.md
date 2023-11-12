---
layout: page
title: common/mkfile (中文)
description: "创建一个或多个任意大小的空文件。"
content_hash: d6daa3b7f61822b48a740267a495829317048b93
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mkfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfile

创建一个或多个任意大小的空文件。
更多信息：<https://manned.org/mkfile>.

- 创建一个 15 千字节的空文件：

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 创建给定大小和单位的文件（bytes, KB, MB, GB）：

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">大小</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 创建两个 4 兆字节的文件：

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名 2</span>
