---
layout: page
title: common/adb-install (한국어)
description: "안드로이드 디버그 브릿지 설치: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에 패키지를 삽입."
content_hash: 397f17d33b0e161824154508120b71b672a94cc5
last_modified_at: 2024-09-07
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb install

안드로이드 디버그 브릿지 설치: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에 패키지를 삽입.
더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터/장치에 안드로이드 애플리케이션 삽입:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 특정 에뮬레이터/장치에 안드로이드 애플리케이션 삽입 ( `$ANDROID_SERIAL`를 재정의):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시리얼_번호</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 데이터를 유지하면서, 기존 앱을 다시 설치([r]einstall):

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 버전 코드 다운그레이드([d]owngrade)를 허용하는 안드로이드 애플리케이션 삽입(디버깅 가능한 패키지만 해당):

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 애플리케이션 매니페스트에 나열된 모든 권한을 부여([g]rant):

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 변경된 APK 부분만 업데이트하여, 설치된 패키지를 빠르게 업데이트:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>
