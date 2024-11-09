---
layout: page
title: linux/agetty (한국어)
description: "대안 `getty`: `tty` 포트를 열고 로그인 이름을 요청한 후 `/bin/login` 명령을 호출합니다."
content_hash: 5cad2c3217349feb7f0cc11e6c958b6df7be3dc3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/agetty.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/agetty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agetty

대안 `getty`: `tty` 포트를 열고 로그인 이름을 요청한 후 `/bin/login` 명령을 호출합니다.
일반적으로 `init`에 의해 호출됩니다.
참고: 보드레이트는 터미널과 장치 간의 직렬 연결을 통한 데이터 전송 속도입니다.
더 많은 정보: <https://manned.org/agetty>.

- `stdin`을 포트(`/dev` 상대 경로)에 연결하고 선택적으로 보드레이트를 지정(기본값: 9600):

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- `stdin`이 이미 `tty`에 연결되었다고 가정하고 로그인에 대한 타임아웃 설정:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timeout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타임아웃_초</span>` -`

- `tty`가 [8]비트라고 가정하고 `init`에 의해 설정된 `TERM` 환경 변수를 재정의:

`agetty -8 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">term_var</span>

- 로그인을 건너뛰고(로그인 없음) 루트 권한으로 다른 로그인 프로그램을 `/bin/login` 대신 호출:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--skip-login</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--login-program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그인_프로그램</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>

- 로그인 프롬프트를 작성하기 전에 사전 로그인(이슈) 파일(`/etc/issue` 기본값)을 표시하지 않음:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--noissue</span>` -`

- 루트 디렉터리를 변경하고 `utmp` 파일에 특정 가짜 호스트 작성:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/루트_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가짜_호스트</span>` -`
