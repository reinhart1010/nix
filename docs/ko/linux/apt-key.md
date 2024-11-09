---
layout: page
title: linux/apt-key (한국어)
description: "Debian 및 Ubuntu의 APT 패키지 관리자를 위한 키 관리 도구."
content_hash: 6ef93eb4452b427fb46a2dc48bef36fb35c3dab6
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/apt-key.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-key.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Debian 및 Ubuntu의 APT 패키지 관리자를 위한 키 관리 도구.
참고: `apt-key`는 이제 더 이상 사용되지 않습니다 (`apt-key del`의 유지 보수 스크립트에서의 사용 제외).
더 많은 정보: <https://manned.org/apt-key.8>.

- 신뢰할 수 있는 키 나열:

`apt-key list`

- 신뢰할 수 있는 키 저장소에 키 추가:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공개_키_파일.asc</span>

- 신뢰할 수 있는 키 저장소에서 키 삭제:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_ID</span>

- 원격 키를 신뢰할 수 있는 키 저장소에 추가:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/filename.key</span>` | apt-key add -`

- 키 ID만 사용하여 키서버에서 키 추가:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEYID</span>
