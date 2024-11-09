---
layout: page
title: linux/urpmq (한국어)
description: "Mageia에서 패키지 및 미디어에 대한 정보를 조회합니다."
content_hash: 4f96fab64ae659e413e18594af6976c671922fbe
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/urpmq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpmq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpmq

Mageia에서 패키지 및 미디어에 대한 정보를 조회합니다.
같이 보기: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpme`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpmq>.

- 설치 가능한 패키지에 대한 정보 표시:

`urpmq -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지의 직접적인 의존성 표시:

`urpmq --requires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지의 직접 및 간접 의존성 표시:

`urpmq --requires-recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- RPM [f]파일에 필요한 설치되지 않은 패키지 및 소스 나열:

`sudo urpmq --requires-recursive -m --sources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.rpm</span>

- URL과 함께 모든 구성된 미디어 나열(비활성 미디어 포함):

`urpmq --list-media --list-url`

- 패키지 검색 시 [g]그룹, 버전 및 [r]릴리즈 출력:

`urpmq -g -r --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 패키지의 정확한 이름을 사용하여 검색:

`urpmq -g -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
