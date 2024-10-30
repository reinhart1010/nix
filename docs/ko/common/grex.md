---
layout: page
title: common/grex (한국어)
description: "정규 표현식을 생성."
content_hash: 90fcb87714311d1bd556cc37a70569fe12a84f9e
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/grex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/grex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grex

정규 표현식을 생성.
더 많은 정보: <https://github.com/pemistahl/grex>.

- 간단한 정규 표현식 생성:

`grex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백으로_구분된_문자열</span>

- 대소문자를 구분하지 않는 정규식을 생성:

`grex -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백으로_구분된_문자열</span>

- 숫자를 '\d'로 변경:

`grex -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백으로_구분된_문자열</span>

- 유니코드 단어 문자를 '\w'로 변경:

`grex -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백으로_구분된_문자열</span>

- 공백을 '\s'로 변경:

`grex -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백으로_구분된_문자열</span>

- 반복되는 하위 문자열에 대한 {min, max} 수량자 표현을 추가:

`grex -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백으로_구분된_문자열</span>
