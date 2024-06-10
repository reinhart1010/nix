---
layout: page
title: linux/pacman4console (한국어)
description: "오리지널 팩맨에서 영감을 받은 텍스트 기반 콘솔 게임."
content_hash: ed6805a1b1d6671805e538a15e96a319bdf74d28
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/linux/pacman4console.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman4console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman4console

오리지널 팩맨에서 영감을 받은 텍스트 기반 콘솔 게임.
더 많은 정보: <https://github.com/YoctoForBeaglebone/pacman4console>.

- 1단계에서 게임 시작:

`pacman4console`

- 특정 단계에서 게임 시작 (총 9개의 공식 단계가 있음):

`pacman4console --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단계_번호</span>

- 지정된 텍스트 파일에 저장하면서 pacman4console 레벨 편집기 시작:

`pacman4consoleedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레벨_파일</span>

- 사용자 정의 레벨 플레이:

`pacman4console --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레벨_파일</span>
