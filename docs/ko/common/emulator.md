---
layout: page
title: common/emulator (한국어)
description: "Android 에뮬레이터 관리."
content_hash: 2b6e287a916f3b56c874d896daceaf46116317f0
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/emulator.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emulator

Android 에뮬레이터 관리.
더 많은 정보: <https://developer.android.com/studio/run/emulator-commandline>.

- Android 에뮬레이터 장치를 시작:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 에뮬레이션에 사용할 수 있는 개발 컴퓨터에 웹캠을 표시:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -webcam-list`

- 후면 카메라 설정을 무시하고 에뮬레이터를 시작 (전면 카메라의 경우 `-camera-front` 사용):

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -camera-back `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|emulated|webcamN</span>

- 최대 네트워크 속도로 에뮬레이터를 시작:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -netspeed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full</span>

- 네트워크 대기 시간이 있는 에뮬레이터를 시작:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -netdelay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none</span>

- 지정된 HTTP/HTTPS 프록시를 통해, 모든 TCP 연결을 만들어 에뮬레이터를 시작 (포트 번호가 필요함):

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -http-proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com:80</span>

- 지정된 SD 카드 파티션 이미지 파일로 에뮬레이터를 시작:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -sdcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/sdcard.img</span>

- 도움말 표시:

`emulator -help`
