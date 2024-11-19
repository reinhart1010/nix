---
layout: page
title: common/unset (中文)
description: "删除 Shell 变量或函数。"
content_hash: 3598f450a7763c222919c02ded968c386923549b
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/unset.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unset.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unset.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unset

删除 Shell 变量或函数。
更多信息：<https://manned.org/unset>.

- 删除变量 `foo`，如果该变量不存在则删除函数 `foo`：

`unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 删除变量 foo 和 bar：

`unset -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 删除函数 my_func：

`unset -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_func</span>
