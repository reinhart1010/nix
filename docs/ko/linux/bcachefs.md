---
layout: page
title: linux/bcachefs (한국어)
description: "`bcachefs` 파일 시스템/장치를 관리합니다."
content_hash: 09202e80b89fa3ccb70e2ae95208bf5a8ae9e886
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bcachefs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bcachefs

`bcachefs` 파일 시스템/장치를 관리합니다.
`device`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://bcachefs-docs.readthedocs.io/en/latest/index.html>.

- `bcachefs`로 파티션 포맷:

`sudo bcachefs format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- `bcachefs` 파일 시스템 마운트:

`sudo bcachefs mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트포인트</span>

- SSD를 캐시로, HDD를 장기 저장소로 사용하는 RAID 0 파일 시스템 생성:

`sudo bcachefs format --label=ssd.ssd1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ssd/파티션</span>` --label=hdd.hdd1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/hdd/파티션</span>` --replicas=1 --foreground_target=ssd --promote_target=ssd --background_target=hdd`

- 다중 장치 파일 시스템 마운트:

`sudo bcachefs mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트포인트</span>

- 디스크 사용량 표시:

`bcachefs fs usage --human-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트포인트</span>

- 포맷 및 마운트 후 복제본 설정:

`sudo bcachefs set-fs-option --metadata_replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --data_replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 모든 파일이 복제되도록 `bcachefs` 강제화:

`sudo bcachefs data rereplicate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트포인트</span>

- 도움말 표시:

`bcachefs`
