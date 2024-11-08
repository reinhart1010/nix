---
layout: page
title: linux/emerge (한국어)
description: "Gentoo Linux 패키지 관리 도구."
content_hash: f15af3410bb18aeddc860b9edd3ee457a925457b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/emerge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/emerge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># emerge

Gentoo Linux 패키지 관리 도구.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- 모든 패키지 동기화:

`emerge --sync`

- 모든 패키지 및 의존성 업데이트:

`emerge -uDNav @world`

- 업데이트 실패 시, 실패한 패키지를 건너뛰고 다시 시작:

`emerge --resume --skipfirst`

- 새 패키지 설치 시, 확인 요청:

`emerge -av `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거 시, 확인 요청:

`emerge -Cav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 고아 패키지 제거 (의존성으로만 설치된 패키지):

`emerge -avc`

- 패키지 데이터베이스에서 키워드 검색:

`emerge -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>
