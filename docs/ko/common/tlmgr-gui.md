---
layout: page
title: common/tlmgr-gui (한국어)
description: "`tlmgr`의 그래픽 사용자 인터페이스를 시작."
content_hash: e323924814bf234726b6089c762260f0bc3fdfe1
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-gui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr gui

`tlmgr`의 그래픽 사용자 인터페이스를 시작.
`tlmgr gui`는 수동으로 설치해야 하는 `perl-tk` 패키지에 의존.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- `tlmgr`를 위한 GUI 시작:

`sudo tlmgr gui`

- 배경색을 지정하여 GUI 시작:

`sudo tlmgr gui -background "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#f39bc3</span>`"`

- 전경색을 지정하여 GUI 시작:

`sudo tlmgr gui -foreground "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#0ef3bd</span>`"`

- 글꼴과 글꼴 크기를 지정하여 GUI 시작:

`sudo tlmgr gui -font "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">helvetica 18</span>`"`

- 특정 크기를 설정하여 GUI 시작:

`sudo tlmgr gui -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x위치</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y위치</span>

- 임의의 X 리소스 문자열을 전달하여 GUI 시작:

`sudo tlmgr gui -xrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xresource</span>
