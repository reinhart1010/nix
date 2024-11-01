---
layout: page
title: common/unimatrix (한국어)
description: "유니코드 문자를 사용하여 매트릭스 느낌을 시뮬레이션."
content_hash: 79c70309277c23a28becd00eea4804b89cc4818c
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/unimatrix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unimatrix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unimatrix

유니코드 문자를 사용하여 매트릭스 느낌을 시뮬레이션.
같이 보기: `cmatrix`.
더 많은 정보: <https://github.com/will8211/unimatrix>.

- `cmatrix`의 기본 출력을 모방 (유니코드 없이, TTY에서 작동):

`unimatrix --no-bold --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">96</span>` --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>

- 볼드체 없이, 느리게, 이모지, 숫자 및 일부 기호 사용:

`unimatrix --no-bold --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ens</span>

- 문자 색상 변경:

`unimatrix --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red|green|blue|white|...</span>

- 문자 집합을 코드로 선택 (`unimatrix --help`에서 사용 가능한 문자 집합 확인):

`unimatrix --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자_집합</span>

- 스크롤 속도 변경:

`unimatrix --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>
