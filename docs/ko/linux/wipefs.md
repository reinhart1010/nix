---
layout: page
title: linux/wipefs (한국어)
description: "파일 시스템, RAID, 또는 파티션 테이블 서명을 장치에서 삭제합니다."
content_hash: da0a903991f689376ee28130e57e1670bf2a11a7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wipefs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wipefs

파일 시스템, RAID, 또는 파티션 테이블 서명을 장치에서 삭제합니다.
더 많은 정보: <https://manned.org/wipefs>.

- 지정된 장치의 서명 표시:

`sudo wipefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 특정 장치의 모든 사용 가능한 서명 유형을 파티션을 재귀적으로 탐색하지 않고 삭제:

`sudo wipefs --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 글롭 패턴을 사용하여 장치 및 파티션의 모든 사용 가능한 서명 유형 삭제:

`sudo wipefs --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>`*`

- 시뮬레이션 실행:

`sudo wipefs --all --no-act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 파일 시스템이 마운트되어 있어도 강제로 삭제:

`sudo wipefs --all --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
