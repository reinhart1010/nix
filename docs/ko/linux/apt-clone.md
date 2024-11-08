---
layout: page
title: linux/apt-clone (한국어)
description: "Debian 기반 시스템의 패키지 상태를 복제/백업/복원합니다."
content_hash: 49989f79e1705eae8ee912517480f4a8ee5ba48e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/apt-clone.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-clone.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-clone

Debian 기반 시스템의 패키지 상태를 복제/백업/복원합니다.
더 많은 정보: <https://github.com/mvo5/apt-clone>.

- 현재 시스템의 패키지 상태를 지정한 디렉터리에 복제:

`apt-clone clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 백업 용도로 클론 파일 (`tar.gz`) 생성:

`apt-clone clone --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업.tar.gz</span>

- 클론 파일에서 패키지 상태 복원:

`apt-clone restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업.tar.gz</span>

- 클론 파일에 대한 정보 표시 (예: 릴리스, 아키텍처):

`apt-clone info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업.tar.gz</span>

- 클론 파일을 현재 시스템에서 복원할 수 있는지 확인:

`apt-clone restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업.tar.gz</span>` --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복원</span>
