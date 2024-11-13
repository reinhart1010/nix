---
layout: page
title: common/dot (한국어)
description: "`graphviz` 파일로부터 `선형 방향` 네트워크 그래프를 렌더링."
content_hash: 81d4506138ec56a6c63d9e2b91f51f5e69bbbbd4
last_modified_at: 2024-11-13
related_topics:
  - title: English version
    url: /en/common/dot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dot

`graphviz` 파일로부터 `선형 방향` 네트워크 그래프를 렌더링.
레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage`, `patchwork`.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일명과 출력 포맷에 기반한 파일명으로 PNG 이미지 렌더링(대문자 -O 사용):

`dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일명.gv</span>

- 지정된 출력 파일명으로 SVG 이미지 렌더링(소문자 -o 사용):

`dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일명.gv</span>

- PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, DOT 포맷으로 출력물을 렌더링:

`dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일명.gv</span>

- `stdin`과 `stdout`을 사용해 GIF 이미지를 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 도움말을 표시:

`dot -?`
