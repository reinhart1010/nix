---
layout: page
title: common/factor (한국어)
description: "숫자의 소인수분해를 출력."
content_hash: 86617ad275d9ee4044e801f2f3a781be86e90b18
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/factor.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/factor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/factor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># factor

숫자의 소인수분해를 출력.
더 많은 정보: <https://www.gnu.org/software/coreutils/factor>.

- 숫자의 소인수분해를 표시:

`factor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 인수가 지정되지 않은 경우, `stdin`에서 입력을 가져옴:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` | factor`
