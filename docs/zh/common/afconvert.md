---
layout: page
title: common/afconvert (中文)
description: "在 AFF 和 raw 文件格式之间进行转换。"
content_hash: d5559f442bae180939a3db6976aca283c7631c64
last_modified_at: 2023-01-06
related_topics:
  - title: English version
    url: /en/common/afconvert.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># afconvert

在 AFF 和 raw 文件格式之间进行转换。
更多信息: <https://manned.org/afconvert.1>.

- 使用一个特定的扩展名（默认：`aff`）：

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">扩展名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件1 路径/到/输出文件2 ...</span>

- 使用一个特定的压缩级别（默认：`7`）：

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件1 路径/到/输出文件2 ...</span>
