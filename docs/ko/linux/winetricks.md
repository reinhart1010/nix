---
layout: page
title: linux/winetricks (한국어)
description: "Wine 가상 Windows 환경 관리 도구."
content_hash: 5799afd27f57bab7cdc2101af3a28898be30b6fc
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/winetricks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# winetricks

Wine 가상 Windows 환경 관리 도구.
더 많은 정보: <https://wiki.winehq.org/Winetricks>.

- 기본 Wine 위치에서 그래픽 설정 시작:

`winetricks`

- 사용자 지정 Wine 디렉터리를 지정하여 Winetricks 실행:

`WINEPREFIX=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/wine_폴더</span>` winetricks`

- 기본 Wine 디렉터리에 Windows DLL 또는 구성 요소 설치:

`winetricks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
