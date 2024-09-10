---
layout: page
title: common/arduino (한국어)
description: "Arduino Studio - Arduino 플랫폼을 위한 통합 개발 환경."
content_hash: ee2c5d8f922cbd9758457482724a4fd0d4eca0ab
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/common/arduino.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/arduino.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino

Arduino Studio - Arduino 플랫폼을 위한 통합 개발 환경.
더 많은 정보: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- 스케치 작성:

`arduino --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ino</span>

- 스케치를 작성하고 업로드:

`arduino --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ino</span>

- Atmega328p CPU가 장착된 Arduino Nano에 스케치를 빌드하고 업로드, 포트 `/dev/ttyACM0`에 연결됨:

`arduino --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:avr:nano:cpu=atmega328p</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyACM0</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ino</span>

- 환경 설정 `name`을 주어진 `value`로 설정:

`arduino --pref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 스케치를 빌드하고 빌드 결과를 빌드 디렉터리에 넣고, 해당 디렉토리에 있는 이전 빌드 결과를 재사용:

`arduino --pref build.path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉터리</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ino</span>

- (변경된) 기본 설정을 `preferences.txt`에 저장:

`arduino --save-prefs`

- 최신 SAM 보드 설치:

`arduino --install-boards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:sam</span>`"`

- Bridge 및 Servo 라이브러리 설치:

`arduino --install-library "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bridge:1.0.0,Servo:1.2.0</span>`"`
