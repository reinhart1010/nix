---
layout: page
title: linux/bcachefs-device (한국어)
description: "실행 중인 `bcachefs` 파일 시스템 내에서 장치를 관리합니다."
content_hash: 9a87f979cb8a585397d5ccca2d023ef3d81c1afb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bcachefs-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bcachefs device

실행 중인 `bcachefs` 파일 시스템 내에서 장치를 관리합니다.
더 많은 정보: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>.

- 기존 파일 시스템에 새 장치를 포맷하고 추가:

`sudo bcachefs device add --label=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>

- 제거를 준비하기 위해 장치의 데이터를 마이그레이션:

`bcachefs device evacuate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>

- 파일 시스템에서 장치를 영구적으로 제거:

`bcachefs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>
