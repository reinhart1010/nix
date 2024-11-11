---
layout: page
title: linux/synopkg (한국어)
description: "Synology DiskStation Manager의 패키지 관리 도구."
content_hash: 4e44976236c3b8a11576146b6667575d16882874
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/synopkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/synopkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># synopkg

Synology DiskStation Manager의 패키지 관리 도구.
더 많은 정보: <https://www.synology.com/dsm>.

- 설치된 패키지의 이름 나열:

`synopkg list --name`

- 특정 패키지에 의존하는 패키지 나열:

`synopkg list --depend-on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 시작/중지:

`sudo synopkg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 상태 출력:

`synopkg status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`sudo synopkg uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 업데이트 가능 여부 확인:

`synopkg checkupdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 패키지를 최신 버전으로 업그레이드:

`sudo synopkg upgradeall`

- synopkg 파일에서 패키지 설치:

`sudo synopkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.spk</span>
