---
layout: page
title: linux/dnf-config-manager (한국어)
description: "Fedora 기반 시스템에서 DNF 구성 옵션과 저장소를 관리합니다."
content_hash: 8367152c243c1e7dc349b4fdace18152eab2823f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dnf-config-manager.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf-config-manager.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf config-manager

Fedora 기반 시스템에서 DNF 구성 옵션과 저장소를 관리합니다.
더 많은 정보: <https://manned.org/dnf-config-manager>.

- URL에서 저장소 추가(그리고 활성화):

`dnf config-manager --add-repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_URL</span>

- 현재 구성 값 출력:

`dnf config-manager --dump`

- 특정 저장소 활성화:

`dnf config-manager --set-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_ID</span>

- 지정된 저장소 비활성화:

`dnf config-manager --set-disabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_ID1 저장소_ID2 ...</span>

- 저장소에 대한 구성 옵션 설정:

`dnf config-manager --setopt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 도움말 표시:

`dnf config-manager --help-cmd`
