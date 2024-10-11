---
layout: page
title: windows/virtualboxvm (한국어)
description: "VirtualBox 가상 머신을 관리합니다."
content_hash: a6225a22de78616d0aee07801bc91973cd6f2189
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/windows/virtualboxvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virtualboxvm

VirtualBox 가상 머신을 관리합니다.
더 많은 정보: <https://www.virtualbox.org>.

- 가상 머신 시작:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|uuid</span>

- 전체 화면 모드로 가상 머신 시작:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|uuid</span>` --fullscreen`

- 지정된 DVD 이미지 파일 마운트:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|uuid</span>` --dvd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\이미지_파일</span>

- 디버그 정보가 포함된 명령줄 창 표시:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|uuid</span>` --debug-command-line`

- 일시 중지된 상태로 가상 머신 시작:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|uuid</span>` --start-paused`
