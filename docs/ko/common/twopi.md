---
layout: page
title: common/twopi (한국어)
description: "`graphviz` 파일에서 `방사형` 네트워크 그래프 이미지를 렌더링."
content_hash: 4421b2db0dd323cd9ee154b7a08044111f9aca79
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/twopi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# twopi

`graphviz` 파일에서 `방사형` 네트워크 그래프 이미지를 렌더링.
레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` 및 `patchwork`.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 출력 형식을 기반으로 파일 이름이 결정되는 PNG 이미지 렌더링 (대문자 -O):

`twopi -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- 지정된 출력 파일 이름으로 SVG 이미지 렌더링 (소문자 -o):

`twopi -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON 또는 DOT 형식으로 출력 렌더링:

`twopi -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- `stdin` 및 `stdout`을 사용하여 GIF 이미지 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | twopi -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 도움말 표시:

`twopi -?`
