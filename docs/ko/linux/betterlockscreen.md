---
layout: page
title: linux/betterlockscreen (한국어)
description: "간단하고, 미니멀한 잠금 화면."
content_hash: c5544bb0b62fa1dfb821dab77ba3f8397aa33e0f
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/betterlockscreen.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/betterlockscreen.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/betterlockscreen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/betterlockscreen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# betterlockscreen

간단하고, 미니멀한 잠금 화면.
더 많은 정보: <https://github.com/betterlockscreen/betterlockscreen>.

- 화면 잠금:

`betterlockscreen --lock`

- 잠금 화면 배경 변경:

`betterlockscreen -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- 사용자 지정 텍스트를 표시하며 화면 잠금:

`betterlockscreen -l pixel -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 지정 잠금 화면 텍스트</span>`"`

- 사용자 지정 모니터 꺼짐 시간(초)을 설정하여 화면 잠금:

`betterlockscreen --off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l`
