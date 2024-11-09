---
layout: page
title: linux/uname (한국어)
description: "Uname은 실행 중인 머신 및 운영 체제 정보를 출력합니다."
content_hash: c90fb502253ef851320be77927bfe63d48b14c78
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/uname.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/uname.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/uname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/uname.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/uname.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/uname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uname

Uname은 실행 중인 머신 및 운영 체제 정보를 출력합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html>.

- 모든 정보 출력:

`uname --all`

- 현재 커널 이름 출력:

`uname --kernel-name`

- 현재 네트워크 노드 호스트명 출력:

`uname --nodename`

- 현재 커널 릴리스 출력:

`uname --kernel-release`

- 현재 커널 버전 출력:

`uname --kernel-version`

- 현재 머신 하드웨어 이름 출력:

`uname --machine`

- 현재 프로세서 유형 출력:

`uname --processor`

- 현재 운영 체제 이름 출력:

`uname --operating-system`
