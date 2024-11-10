---
layout: page
title: linux/wl-copy (한국어)
description: "Wayland 클립보드에 복사 및 지우기."
content_hash: fe65702c78089ee03f2dc21a9637e19434918b22
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wl-copy.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/wl-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wl-copy

Wayland 클립보드에 복사 및 지우기.
같이 보기: `wl-paste`, `xclip`.
더 많은 정보: <https://github.com/bugaevc/wl-clipboard>.

- 텍스트를 클립보드에 복사:

`wl-copy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`"`

- 명령어 (`ls`) 출력을 파이프로 클립보드에 복사:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | wl-copy`

- 한 번만 붙여넣기 후 클립보드를 지우기:

`wl-copy --paste-once "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`"`

- 이미지를 복사:

`wl-copy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 클립보드 지우기:

`wl-copy --clear`
