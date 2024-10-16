---
layout: page
title: common/eval (한국어)
description: "현재 쉘에서 인수를 단일 명령으로 실행하고 그 결과를 반환."
content_hash: 1f5a18b34cb9a04790e0b5544a3a7371217a8071
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/eval.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/eval.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/eval.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eval

현재 쉘에서 인수를 단일 명령으로 실행하고 그 결과를 반환.
더 많은 정보: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>.

- "foo" 인수를 사용하여 `echo`를 호출:

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo foo</span>`"`

- 현재 쉘에서 변수를 설정:

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo=bar</span>`"`
