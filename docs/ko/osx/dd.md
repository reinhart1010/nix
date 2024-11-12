---
layout: page
title: osx/dd (한국어)
description: "파일을 변환하고 복사합니다."
content_hash: d466893cb1a0175653f772cf2fc4f9ba032ab891
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

파일을 변환하고 복사합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- 부팅 가능한 USB 드라이브를 isohybrid 파일(예: `archlinux-xxx.iso`)로 만들고 진행률 표시:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_드라이브</span>` status=progress`

- 드라이브를 다른 드라이브로 4MB 블록 단위로 복제하고 오류를 무시하며 진행률 표시:

`dd bs=4m conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/소스_드라이브</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/대상_드라이브</span>` status=progress`

- 커널 랜덤 드라이버를 사용하여 특정 바이트 수의 랜덤 데이터를 가진 파일 생성:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/랜덤_파일</span>

- 디스크의 쓰기 성능을 벤치마킹:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/1GB_파일</span>

- 시스템 백업을 생성하여 IMG 파일로 저장하고 나중에 `if`와 `of`를 교환하여 복원 가능하며 진행률 표시:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/드라이브_디바이스</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.img</span>` status=progress`

- 진행 중인 `dd` 작업의 진행률 확인 (다른 셸에서 이 명령 실행):

`kill -USR1 $(pgrep ^dd)`
