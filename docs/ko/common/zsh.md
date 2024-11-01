---
layout: page
title: common/zsh (한국어)
description: "Z SHell, Bash 호환 명령줄 인터프리터."
content_hash: 99136ccd85a9bff0926399d7607f91cb5460b0ed
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zsh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zsh

Z SHell, Bash 호환 명령줄 인터프리터.
같이 보기: `bash`, `histexpand`.
더 많은 정보: <https://www.zsh.org>.

- 대화형 셸 세션 시작:

`zsh`

- 특정 [c]명령 실행:

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>`"`

- 특정 스크립트 실행:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.zsh</span>

- 특정 스크립트를 실행하지 않고 구문 오류 검사:

`zsh --no-exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.zsh</span>

- `stdin`에서 특정 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>` | zsh`

- 특정 스크립트를 실행하며 각 명령을 실행 전에 출력:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.zsh</span>

- 대화형 셸 세션을 자세한 모드로 시작하여 실행 전 각 명령 출력:

`zsh --verbose`

- `zsh` 내에서 특정 명령을 글로브 패턴 비활성화하여 실행:

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
