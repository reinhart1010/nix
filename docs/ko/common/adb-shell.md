---
layout: page
title: common/adb-shell (한국어)
description: "안드로이드 디버그 브릿지 쉘: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에서 원격 쉘 명령을 실행."
content_hash: 34b76e30b6b25a2992f966a64c9ae451aabb151a
last_modified_at: 2024-09-06
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-shell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-shell.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

안드로이드 디버그 브릿지 쉘: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에서 원격 쉘 명령을 실행.
더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터 또는 장치에서 원격 대화형 셸을 시작:

`adb shell`

- 에뮬레이터 또는 장치에서 모든 속성을 가져옴:

`adb shell getprop`

- 모든 런타임 권한을 기본 값으로 복구:

`adb shell pm reset-permissions`

- 애플리케이션에 대한 위험한 권한 취소:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">권한</span>

- 키보드 이벤트 트리거:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키코드</span>

- 에뮬레이터 또는 장치에서 애플리케이션 데이터 지우기:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 에뮬레이터 또는 장치에서 액티비티 컴포넌트 시작:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">활동</span>

- 에뮬레이터 또는 기기에서 홈 액티비티 컴포넌트 시작:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
