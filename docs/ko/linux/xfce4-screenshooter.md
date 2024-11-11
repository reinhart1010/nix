---
layout: page
title: linux/xfce4-screenshooter (한국어)
description: "XFCE4 스크린샷 도구."
content_hash: 722a04fe1c4e2a506cdec7e0416b8e40e1a5af4b
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/xfce4-screenshooter.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xfce4-screenshooter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xfce4-screenshooter

XFCE4 스크린샷 도구.
더 많은 정보: <https://docs.xfce.org/apps/xfce4-screenshooter/start>.

- 스크린샷 GUI 시작:

`xfce4-screenshooter`

- 전체 화면을 캡처하고 GUI를 시작하여 다음 단계를 선택:

`xfce4-screenshooter --fullscreen`

- 전체 화면을 캡처하고 지정된 폴더에 저장:

`xfce4-screenshooter --fullscreen --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 스크린샷을 찍기 전까지 대기:

`xfce4-screenshooter --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>

- 화면의 특정 영역을 캡처 (마우스를 사용하여 선택):

`xfce4-screenshooter --region`

- 활성 창을 캡처하고 클립보드에 복사:

`xfce4-screenshooter --window --clipboard`

- 활성 창을 캡처하고 선택한 프로그램으로 열기:

`xfce4-screenshooter --window --open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gimp</span>
