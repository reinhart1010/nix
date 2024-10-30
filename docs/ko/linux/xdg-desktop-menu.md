---
layout: page
title: linux/xdg-desktop-menu (한국어)
description: "데스크탑 메뉴 항목을 설치하거나 제거하는 명령줄 도구."
content_hash: f70c8216b9b096376c9059531f4d8a01f88f0184
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xdg-desktop-menu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xdg-desktop-menu

데스크탑 메뉴 항목을 설치하거나 제거하는 명령줄 도구.
더 많은 정보: <https://manned.org/xdg-desktop-menu>.

- 애플리케이션을 데스크탑 메뉴 시스템에 설치:

`xdg-desktop-menu install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.desktop</span>

- 벤더 접두사 확인을 비활성화하고 애플리케이션을 데스크탑 메뉴 시스템에 설치:

`xdg-desktop-menu install --novendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.desktop</span>

- 애플리케이션을 데스크탑 메뉴 시스템에서 제거:

`xdg-desktop-menu uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.desktop</span>

- 데스크탑 메뉴 시스템 강제 업데이트:

`xdg-desktop-menu forceupdate --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|system</span>
