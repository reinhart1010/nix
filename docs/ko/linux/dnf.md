---
layout: page
title: linux/dnf (한국어)
description: "RHEL, Fedora 및 CentOS를 위한 패키지 관리 도구(yum을 대체)."
content_hash: 73327c4758a62814782ea4764495864578c4dc37
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf

RHEL, Fedora 및 CentOS를 위한 패키지 관리 도구(yum을 대체).
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://dnf.readthedocs.io>.

- 설치된 패키지를 최신 버전으로 업그레이드:

`sudo dnf upgrade`

- 키워드를 통해 패키지 검색:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드1 키워드2 ...</span>

- 패키지에 대한 세부 정보 표시:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 새 패키지 설치 (`-y`를 사용하여 모든 프롬프트 자동 확인):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 패키지 제거:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 설치된 패키지 나열:

`dnf list --installed`

- 특정 명령을 제공하는 패키지 찾기:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 모든 과거 작업 보기:

`dnf history`
