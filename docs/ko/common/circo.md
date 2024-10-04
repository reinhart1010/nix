---
layout: page
title: common/circo (한국어)
description: "`graphviz` 파일에서 `circular` 네트워크 그래프의 이미지를 렌더링."
content_hash: 3aaccee68dcb75d6397e4a9a03101836f30715e7
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/circo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# circo

`graphviz` 파일에서 `circular` 네트워크 그래프의 이미지를 렌더링.
레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름 및 출력 형식(대문자 -O)을 기반으로 하는 파일 이름으로 PNG 이미지를 렌더링:

`circo -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- 지정된 출력 파일명으로 SVG(소문자 -o) 이미지를 렌더링:

`circo -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- 출력을 PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, 또는 DOT 형식으로 렌더링:

`circo -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포맷</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- `stdin` 및 `stdout`을 사용하여 GIF 이미지 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | circo -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 도움말 표시:

`circo -?`
