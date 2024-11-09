---
layout: page
title: linux/vso (한국어)
description: "Vanilla OS를 위한 패키지 관리자, 시스템 업데이트 및 작업 자동화 도구."
content_hash: 5a8c1464b4fa494708c37c7018f0a5819a54d584
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vso.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vso.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vso

Vanilla OS를 위한 패키지 관리자, 시스템 업데이트 및 작업 자동화 도구.
더 많은 정보: <https://github.com/Vanilla-OS/vanilla-system-operator>.

- 호스트 시스템의 시스템 업데이트 확인:

`vso sys-upgrade check`

- 호스트 시스템을 지금 업그레이드:

`vso sys-upgrade upgrade --now`

- Pico 하위 시스템 초기화 (패키지 관리에 사용됨):

`vso pico-init`

- 하위 시스템 내 애플리케이션 설치:

`vso install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 하위 시스템에서 애플리케이션 제거:

`vso remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 하위 시스템의 셸에 진입:

`vso shell`

- 하위 시스템에서 애플리케이션 실행:

`vso run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- VSO 구성 표시:

`vso config show`
