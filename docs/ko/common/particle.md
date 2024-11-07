---
layout: page
title: common/particle (한국어)
description: "Particle 장치를 조작."
content_hash: 0e865a891c581798d0d3347a3efb5040c21c33fd
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/particle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/particle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># particle

Particle 장치를 조작.
더 많은 정보: <https://docs.particle.io/tutorials/developer-tools/cli>.

- Particle CLI에 로그인하거나 계정 생성:

`particle setup`

- 장치 목록 표시:

`particle list`

- 대화형으로 새 Particle 프로젝트 생성:

`particle project create`

- Particle 프로젝트 컴파일:

`particle compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_코드.ino</span>

- 특정 앱을 원격으로 사용하도록 장치 업데이트:

`particle flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로그램.bin</span>

- 최신 펌웨어로 장치를 시리얼로 업데이트:

`particle flash --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/방화벽.bin</span>

- 장치에서 함수 실행:

`particle call `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_인자</span>
