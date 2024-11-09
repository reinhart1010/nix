---
layout: page
title: linux/cloud-init (한국어)
description: "클라우드 인스턴스 초기화를 관리하는 명령줄 도구."
content_hash: 9432671ce8c2d875244a95b0ae5f1c0010ceb4ff
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cloud-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cloud-init

클라우드 인스턴스 초기화를 관리하는 명령줄 도구.
더 많은 정보: <https://cloudinit.readthedocs.io>.

- 가장 최근에 실행된 cloud-init의 상태 표시:

`cloud-init status`

- cloud-init 실행이 완료될 때까지 대기 후 상태 보고:

`cloud-init status --wait`

- 쿼리할 수 있는 상위 수준 메타데이터 키 목록 표시:

`cloud-init query --list-keys`

- 캐시된 인스턴스 메타데이터 쿼리:

`cloud-init query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">점_구분_변수_경로</span>

- cloud-init이 다시 실행될 수 있도록 로그 및 아티팩트 정리:

`cloud-init clean`
