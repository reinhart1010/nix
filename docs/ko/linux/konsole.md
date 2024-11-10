---
layout: page
title: linux/konsole (한국어)
description: "KDE의 터미널 에뮬레이터."
content_hash: bcca9f113fb9776dfe220bc1099be1470840e4cb
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/konsole.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/konsole.html
    icon: bi bi-globe
tldri18n_status: 2
---
# konsole

KDE의 터미널 에뮬레이터.
더 많은 정보: <https://docs.kde.org/stable5/en/konsole/konsole/command-line-options.html>.

- 특정 디렉토리에서 터미널 열기:

`konsole --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 명령을 [e]실행하고 종료 후 창 닫지 않기:

`konsole --noclose -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`

- 새 탭 열기:

`konsole --new-tab`

- 백그라운드에서 터미널을 열고 `Ctrl+Shift+F12`를 누르면 앞으로 가져오기:

`konsole --background-mode`
