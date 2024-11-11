---
layout: page
title: linux/xmount (한국어)
description: "여러 입력 및 출력 하드 디스크 이미지 형식을 선택적 쓰기 캐시 지원과 함께 실시간으로 변환합니다."
content_hash: c2bc83ed0c1cb75c9c440988330e8cf7ef52d08a
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/xmount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xmount

여러 입력 및 출력 하드 디스크 이미지 형식을 선택적 쓰기 캐시 지원과 함께 실시간으로 변환합니다.
FUSE(Filesystem in Userspace)를 사용하여 입력 이미지의 가상 표현을 포함하는 가상 파일 시스템을 만듭니다.
더 많은 정보: <https://manned.org/xmount>.

- `.raw` 이미지 파일을 DMG 컨테이너 파일로 마운트:

`xmount --in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.dd</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dmg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_포인트</span>

- 쓰기-캐시 지원과 함께 EWF 이미지 파일을 VHD 파일로 마운트하여 부팅:

`xmount --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/캐시.ovl</span>` --in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ewf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.E??</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vhd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_포인트</span>

- 섹터 2048의 첫 번째 파티션을 새 `.raw` 이미지 파일로 마운트:

`xmount --offset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` --in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.dd</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_포인트</span>
