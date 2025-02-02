---
layout: page
title: common/adb (한국어)
description: "안드로이드 디버그 브릿지: 안드로이드 에뮬레이터 객체 또는 연결된 안드로이드 장치와 통신."
content_hash: eb0d72b1f36c00b94a8aa98bd307d0f3ec3e35d5
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb

안드로이드 디버그 브릿지: 안드로이드 에뮬레이터 객체 또는 연결된 안드로이드 장치와 통신.
더 많은 정보: <https://developer.android.com/tools/adb>.

- adb 서버 프로세스가 실행되고 있고, 시작하는지 확인:

`adb start-server`

- adb 서버 프로세스 종료:

`adb kill-server`

- 대상 에뮬레이터/장치 객체에서 원격 쉘 시작:

`adb shell`

- 안드로이드 애플리케이션을 에뮬레이터/장치로 푸쉬:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.apk</span>

- 대상 장치에서부터 파일/디렉토리를 복사:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/장치_파일명_또는_디렉토리명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/로컬_목적지_디렉토리명</span>

- 대상 장치로 파일/디렉토리 복사:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/로컬_파일명_또는_디렉토리명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/장치_목적지_directory</span>

- 연결된 장치들의 목록 가져오기:

`adb devices`
