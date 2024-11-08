---
layout: page
title: linux/debtap (한국어)
description: "Debian 패키지를 Arch Linux 패키지로 변환합니다."
content_hash: 4f0bb6bb4226af44fb60ddb9bb0118196aed4e55
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/debtap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debtap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debtap

Debian 패키지를 Arch Linux 패키지로 변환합니다.
같이 보기: `pacman-upgrade`.
더 많은 정보: <https://github.com/helixarch/debtap>.

- debtap 데이터베이스 업데이트 (최초 실행 전):

`sudo debtap --update`

- 지정된 패키지 변환:

`debtap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>

- 메타데이터 파일 편집을 제외한 모든 질문을 건너뛰고 지정된 패키지 변환:

`debtap --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>

- PKGBUILD 파일 생성:

`debtap --pkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>
