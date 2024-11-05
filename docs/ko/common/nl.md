---
layout: page
title: common/nl (한국어)
description: "파일 또는 `stdin`에서 각 행에 번호를 매깁니다."
content_hash: cf9c629d9baa26e5844bcd90fdedfbe46ff97dac
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nl

파일 또는 `stdin`에서 각 행에 번호를 매깁니다.
더 많은 정보: <https://manned.org/nl.1p>.

- 파일에서 빈 줄이 아닌 행에 번호 매기기:

`nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 읽기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | nl -`

- 빈 줄을 포함한 [a]ll [b]ody 행에 번호를 매기거나 [n]ot [b]ody 행에 번호를 매기지 않음:

`nl -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 기본 정규 표현식(BRE) [p]attern과 일치하는 [b]ody 행에만 번호 매기기:

`nl -b p'FooBar[0-9]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 [i]ncrement로 행 번호 매기기:

`nl -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">증가량</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 행 번호 형식을 [r]ight 또는 [l]eft로 정렬하고 선행 [z]eros를 유지하거나 [n]ot:

`nl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rz|ln|rn</span>

- 행 번호의 [w]idth 지정 (기본값은 6):

`nl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 행 번호와 행 사이를 구분하기 위한 특정 문자열 사용 (기본값은 TAB):

`nl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
