---
layout: page
title: linux/cryptsetup-luksformat (한국어)
description: "LUKS 파티션과 초기 키 슬롯(0)을 암호 또는 키파일로 초기화합니다."
content_hash: 79466aae361a50ad2599843a453d1840a3ab560b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cryptsetup-luksformat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cryptsetup luksFormat

LUKS 파티션과 초기 키 슬롯(0)을 암호 또는 키파일로 초기화합니다.
참고: 이 작업은 파티션의 모든 데이터를 덮어씁니다.
더 많은 정보: <https://manned.org/cryptsetup-luksFormat>.

- 암호로 LUKS 볼륨 초기화:

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 키파일로 LUKS 볼륨 초기화:

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키파일</span>

- 암호로 LUKS 볼륨 초기화하고 라벨 설정:

`cryptsetup luksFormat --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
