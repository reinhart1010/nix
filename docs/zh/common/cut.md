---
layout: page
title: common/cut (中文)
description: "从标准输入或文件中剪切字段。"
content_hash: 5cba33ec765fe01e8ce6376987aac2746e2666b4
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/cut.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

从标准输入或文件中剪切字段。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- 打印每行的特定字符/或属性范围：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters|fields</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- 打印每行由指定分隔符分割的属性范围：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | cut --delimiter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分隔符</span>`" --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- 打印文件每行的字符范围：

`cut --characters `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 打印以 `NUL` 结尾的行的特定字段（例如 `find . -print0`）而不是换行符：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | cut --zero-terminated --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
