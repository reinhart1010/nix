---
layout: page
title: linux/cryptsetup-open (한국어)
description: "암호화된 볼륨의 암호 해독된 매핑 생성."
content_hash: 680220d4fdb1ca034f85bea6dc2a8e88f6473b84
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cryptsetup-open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cryptsetup open

암호화된 볼륨의 암호 해독된 매핑 생성.
참고: TRIM이 활성화된 경우, 해방된 블록 정보의 형태로 최소한의 데이터 누출이 발생할 수 있으며, 사용 중인 파일 시스템을 파악하는 데 충분할 수 있습니다.
그러나 데이터 자체는 여전히 안전하며, TRIM이 없는 SSD는 더 빨리 마모되므로 TRIM을 활성화하는 것이 좋습니다.
더 많은 정보: <https://manned.org/cryptsetup-open>.

- LUKS 볼륨을 열고 `/dev/mapper/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>에 암호 해독된 매핑 생성:

`cryptsetup open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- 암호 대신 키 파일 사용:

`cryptsetup open --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- 장치에서 TRIM 사용 허용:

`cryptsetup open --allow-discards `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- LUKS 헤더에 `--allow-discards` 옵션 기록 (장치를 열 때마다 항상 이 옵션 사용):

`cryptsetup open --allow-discards --persistent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- LUKS 볼륨을 열고 암호 해독된 매핑을 읽기 전용으로 설정:

`cryptsetup open --readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>
