---
layout: page
title: linux/kpackagetool5 (한국어)
description: "K패키지 관리자: Plasma 패키지 설치, 나열, 제거."
content_hash: 6fdc8839ea4be24e3b80cf1898cecf88779b56af
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/kpackagetool5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kpackagetool5

K패키지 관리자: Plasma 패키지 설치, 나열, 제거.
더 많은 정보: <https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>.

- 설치 가능한 모든 패키지 유형 나열:

`kpackagetool5 --list-types`

- 디렉토리에서 패키지 설치:

`kpackagetool5 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_유형</span>` --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉토리에서 설치된 패키지 업데이트:

`kpackagetool5 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_유형</span>` --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 설치된 플라스모이드 나열 (--global로 모든 사용자에 대해 표시):

`kpackagetool5 --type Plasma/Applet --list --global`

- 이름으로 플라스모이드 제거:

`kpackagetool5 --type Plasma/Applet --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`"`
