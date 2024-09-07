---
layout: page
title: common/adb-logcat (한국어)
description: "시스템 메시지의 로그 덤프."
content_hash: 5b515a675888b269df1df747fd561e5a9be1659f
last_modified_at: 2024-09-07
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb logcat

시스템 메시지의 로그 덤프.
더 많은 정보: <https://developer.android.com/tools/logcat>.

- 시스템 로그 표시:

`adb logcat`

- 정규 표현식([e]xpression)과 일치하는 행 표시:

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 특정 모드(상세 ([V]erbose), 디버그([D]ebug), 정보([I]nfo), 경고([W]arning), 에러([E]rror), 치명적 오류([F]atal), 무음([S]ilent))에서 태그에 대한 로그를 표시하고 다른 태그를 필터링:

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모드</span>` *:S`

- 다른 태그를 무음으로([S]ilencing), 상세 ([V]erbose) 모드에서 React Native 애플리케이션에 대한 로그를 표시:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- 우선순위 수준이 경고([W]arning) 이상인 모든 태그에 대한 로그 표시:

`adb logcat *:W`

- 특정 PID에 대한 로그 표시:

`adb logcat --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 특정 패키지의 프로세스에 대한 로그 표시:

`adb logcat --pid $(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`)`

- 로그 색상 지정(보통 필터와 함께 사용):

`adb logcat -v color`
