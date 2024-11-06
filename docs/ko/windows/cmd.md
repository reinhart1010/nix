---
layout: page
title: windows/cmd (한국어)
description: "Windows 명령 인터프리터."
content_hash: 321bbd0d98deb7a2649cf701c97cc5eaedd745b2
last_modified_at: 2024-11-06
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmd

Windows 명령 인터프리터.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- 대화형 셸 세션 시작:

`cmd`

- 특정 [c]ommands 실행:

`cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>

- 특정 스크립트 실행:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\script.bat</span>

- 특정 명령을 실행한 후 대화형 셸로 진입:

`cmd /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>

- 명령 출력에서 `echo`가 비활성화된 대화형 셸 세션 시작:

`cmd /q`

- 지연된 [v]ariable 확장이 활성화 또는 비활성화된 대화형 셸 세션 시작:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 명령 [e]xtensions가 활성화 또는 비활성화된 대화형 셸 세션 시작:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- [u]nicode 인코딩을 사용하는 대화형 셸 세션 시작:

`cmd /u`
