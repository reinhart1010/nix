---
layout: page
title: linux/xrandr (한국어)
description: "화면의 출력 크기, 방향 및/또는 반사를 설정."
content_hash: 443a9c32f63061788d4f7f8b2743cc54d8c7e41f
last_modified_at: 2024-10-30
related_topics:
  - title: Deutsch version
    url: /de/linux/xrandr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xrandr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/xrandr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xrandr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xrandr

화면의 출력 크기, 방향 및/또는 반사를 설정.
더 많은 정보: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- 시스템의 현재 상태(알려진 화면, 해상도 등) 표시:

`xrandr --query`

- 연결되지 않은 출력을 비활성화하고 기본 설정으로 연결된 출력 활성화:

`xrandr --auto`

- DisplayPort 1의 해상도와 갱신 빈도를 1920x1080, 60Hz로 변경:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920x1080</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>

- HDMI2의 해상도를 1280x1024로 설정하고 DP1의 오른쪽에 배치:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HDMI2</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1280x1024</span>` --right-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>

- VGA1 출력 비활성화:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VGA1</span>` --off`

- LVDS1의 밝기를 50%로 설정:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LVDS1</span>` --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>

- X 서버의 현재 상태 표시:

`xrandr --display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --query`
