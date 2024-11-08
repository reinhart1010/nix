---
layout: page
title: common/makensis (한국어)
description: "NSIS 설치 프로그램을 위한 크로스 플랫폼 컴파일러."
content_hash: b060de4a0188d06559377635b1b569eb91cf3c2d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/makensis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# makensis

NSIS 설치 프로그램을 위한 크로스 플랫폼 컴파일러.
NSIS 스크립트를 Windows 설치 프로그램 실행 파일로 컴파일합니다.
더 많은 정보: <https://nsis.sourceforge.io/Docs/Chapter3.html>.

- NSIS 스크립트 컴파일:

`makensis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nsi</span>

- 엄격 모드로 NSIS 스크립트 컴파일 (경고를 오류로 처리):

`makensis -WX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nsi</span>

- 특정 명령에 대한 도움말 표시:

`makensis -CMDHELP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
