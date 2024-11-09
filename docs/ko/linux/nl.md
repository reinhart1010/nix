---
layout: page
title: linux/nl (한국어)
description: "파일이나 `stdin`에서 각 줄에 번호를 매깁니다."
content_hash: 9850e6cbf9bad90b03b1b9b6ccb5945dafc10b98
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nl

파일이나 `stdin`에서 각 줄에 번호를 매깁니다.
더 많은 정보: <https://manned.org/nl.1p>.

- 파일에서 빈 줄이 아닌 줄에 번호 매기기:

`nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 읽기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | nl -`

- 빈 줄을 포함한 모든 본문 줄에 번호를 매기거나 본문 줄에 번호를 매기지 않기:

`nl --body-numbering `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 기본 정규 표현식(BRE) 패턴과 일치하는 본문 줄에만 번호 매기기:

`nl --body-numbering p'FooBar[0-9]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 줄 번호 매기기에 특정 [i]크기 사용:

`nl --line-increment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 줄 번호 매기기 형식을 오른쪽 정렬 또는 왼쪽 정렬로 지정하고, 앞쪽에 0을 유지할지 여부 지정:

`nl --number-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rz|ln|rn</span>

- 줄 번호 매기기의 [w]너비 지정 (기본값은 6):

`nl --number-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 줄 번호와 줄을 구분하는 특정 문자열 사용 (기본값은 탭):

`nl --number-separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
