---
layout: page
title: common/ac (中文)
description: "打印用户连接时间的统计数据。"
content_hash: 2e8c0e3c09126fa8f669282bff99c7d0af6286c3
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

打印用户连接时间的统计数据。
更多信息：<https://man.openbsd.org/ac>.

- 打印当前用户连接的时间，以小时为单位：

`ac`

- 打印用户连接的时间，以小时为单位：

`ac -p`

- 打印一个特定用户的连接时间，以小时为单位：

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 打印一个特定用户每天连接的时间，以小时为单位（包括总数）：

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>
