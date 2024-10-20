---
layout: page
title: common/finger (한국어)
description: "사용자 정보조회 프로그램."
content_hash: d52eeb86a5979ede30a22b7a0ffa0054920cd772
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/finger.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/finger.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/finger.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/finger.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># finger

사용자 정보조회 프로그램.
더 많은 정보: <https://manned.org/finger>.

- 현재 로그인한 사용자에 대한 정보 표시:

`finger`

- 특정 사용자에 대한 정보 표시:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 사용자의 로그인 이름, 실명, 단말기 이름 및 기타 정보를 표시:

`finger -s`

- `-s`와 동일한 정보는 물론 사용자의 홈 디렉터리, 집. ㅓㄴ화번호, 로그인 쉘, 메일 상태 등을 표시하는 여러 줄 출력 형식을 생성:

`finger -l`

- 사용자 이름과의 일치를 방지하고 로그인 이름만 사용:

`finger -m`
