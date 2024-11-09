---
layout: page
title: common/sh (한국어)
description: "Bourne 셸, 표준 명령어 언어 해석기."
content_hash: 47751eb6a00bd00f80872303c7d1b89d39aab38a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/sh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sh.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sh

Bourne 셸, 표준 명령어 언어 해석기.
히스토리 확장을 위해 `histexpand`도 참조하세요.
더 많은 정보: <https://manned.org/sh>.

- 대화형 셸 세션 시작:

`sh`

- 명령을 실행하고 종료:

`sh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 스크립트 실행:

`sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- `stdin`에서 명령을 읽고 실행:

`sh -s`
