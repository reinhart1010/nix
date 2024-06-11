---
layout: page
title: linux/dd (한국어)
description: "파일 변환 및 복사."
content_hash: 67e11289b5823f6984bb37a4f5ac0f81b2ef4e9a
last_modified_at: 2024-06-11
related_topics:
  - title: English version
    url: /en/linux/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

파일 변환 및 복사.
더 많은 정보: <https://www.gnu.org/software/coreutils/dd>.

- isohybrid 파일(예: `archlinux-xxx.iso`)에서 부팅 가능한 USB 드라이브를 만들고 진행 상황 표시:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_drive</span>` status=progress`

- 4 MiB 블록이 있는 다른 드라이브에 드라이브를 복제하고, 오류를 무시하고 진행 상황을 표시:

`dd bs=4M conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/소스_드라이브</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/목적지_드라이브</span>` status=progress`

- 커널 랜덤 드라이버를 사용하여, 특정 수의 임의 바이트 크기를 가지는 파일 생성:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/랜덤_파일</span>

- 디스크의 쓰기 성능 벤치마크:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/1GB_파일</span>

- IMG 파일로 시스템 백업을 생성하고 진행 상황 표시:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/드라이브_장치</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.img</span>` status=progress`

- 진행 중인 `dd` 작업의 진행 상황을 확인 (다른 셸에서 이 명령어 실행):

`kill -USR1 $(pgrep -x dd)`
