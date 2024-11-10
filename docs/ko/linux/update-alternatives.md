---
layout: page
title: linux/update-alternatives (한국어)
description: "심볼릭 링크를 편리하게 관리하여 기본 명령을 결정합니다."
content_hash: 97cfebd54c698ed5676918fa09fd680acc608926
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/update-alternatives.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/update-alternatives.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/update-alternatives.html
    icon: bi bi-globe
tldri18n_status: 2
---
# update-alternatives

심볼릭 링크를 편리하게 관리하여 기본 명령을 결정합니다.
더 많은 정보: <https://manned.org/update-alternatives>.

- 심볼릭 링크 추가:

`sudo update-alternatives --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/심볼릭링크</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/명령_바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>

- `java`에 대한 심볼릭 링크 구성:

`sudo update-alternatives --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- 심볼릭 링크 제거:

`sudo update-alternatives --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/opt/java/jdk1.8.0_102/bin/java</span>

- 지정된 명령에 대한 정보 표시:

`update-alternatives --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- 모든 명령과 현재 선택된 항목 표시:

`update-alternatives --get-selections`
