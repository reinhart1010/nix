---
layout: page
title: common/csh (한국어)
description: "C와 유사한 구문을 사용하는 셸 (명령어 인터프리터)."
content_hash: 24fca18ad47a247147862a90a7aa65013064ce3f
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/csh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/csh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/csh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># csh

C와 유사한 구문을 사용하는 셸 (명령어 인터프리터).
참고: `tcsh`.
더 많은 정보: <https://www.mkssoftware.com/docs/man1/csh.1.asp>.

- 대화형 셸 세션을 시작:

`csh`

- 시작 구성을 로드하지 않고 대화형 셸 세션을 시작:

`csh -f`

- 특정 명령어([c]ommands)를 실행:

`csh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'csh가 실행됨'</span>`"`

- 특정 스크립트를 실행:

`csh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.csh</span>
