---
layout: page
title: common/fdp (한국어)
description: "`graphviz` 파일에서 `force-directed` 네트워크 그래프의 이미지를 렌더링."
content_hash: 34b6632dd4a90fddbe399865ee23e045cb5e8118
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fdp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fdp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdp

`graphviz` 파일에서 `force-directed` 네트워크 그래프의 이미지를 렌더링.
레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름 및 출력 형식(대문자 -O)을 기반으로 하는 파일 이름으로 PNG 이미지를 렌더링:

`fdp -T png -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gv</span>

- 지정된 출력 파일 이름 (소문자 -o) SVG 이미지를 렌더링:

`fdp -T svg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gv</span>

- 출력을 특정 형식으로 렌더링:

`fdp -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps|pdf|svg|fig|png|gif|jpg|json|dot</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gv</span>

- `stdin` 및 `stdout`을 사용하여 `gif` 이미지 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | fdp -T gif > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 도움말 표시:

`fdp -?`
