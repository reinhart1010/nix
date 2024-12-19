---
layout: page
title: common/md5sum (中文)
description: "计算 MD5 加密校验和。"
content_hash: 2d08331107ebeee38984054fc04ac7c058e19383
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/common/md5sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/md5sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/md5sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/md5sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/md5sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># md5sum

计算 MD5 加密校验和。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- 计算文件的 MD5 校验和：

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 计算多个文件的 MD5 校验和：

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- 读取 MD5SUM 的文件并验证所有文件是否具有匹配的校验和：

`md5sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md5</span>
