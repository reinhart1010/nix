---
layout: page
title: common/zapier-init (中文)
description: "初始化一个新的 Zapier 集成。"
content_hash: dc87a1bf6ccad00f6167e6945cc90a1e9d2af655
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zapier-init.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zapier-init.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier init

初始化一个新的 Zapier 集成。
更多信息：<https://platform.zapier.com/reference/cli#init>.

- 初始化一个新的 Zapier 集成：

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 使用特定模板初始化一个新的 Zapier 集成：

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic-auth|callback|custom-auth|digest-auth|dynamic-dropdown|files|minimal|oauth1-trello|oauth2|search-or-create|session-auth|typescript</span>

- 显示额外的调试输出：

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
