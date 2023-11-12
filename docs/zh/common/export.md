---
layout: page
title: common/export (中文)
description: "命令为当前 shell 中的子进程进行环境变量设置。"
content_hash: eae310f02f773d826824dab792feb6e617f7633f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/export.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/export.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/export.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># export

命令为当前 shell 中的子进程进行环境变量设置。
更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- 设置为新的环境变量：

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">某变量名</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 删除环境变量：

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">某变量名</span>

- 给 PATH 追加新的路径进去：

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">追加的 path 路径</span>
