---
layout: page
title: common/patchwork (한국어)
description: "`그래프비즈` 파일에서 `squareified treemap` 네트워크 그래프의 이미지를 렌더링합니다."
content_hash: c5b2235c04d30ff17cb3d06ad0d5d4886558ac99
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/patchwork.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/patchwork.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># patchwork

`그래프비즈` 파일에서 `squareified treemap` 네트워크 그래프의 이미지를 렌더링합니다.
레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` 및 `patchwork`.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 출력 형식(대문자 -O)을 기반으로 PNG 이미지를 렌더링:

`patchwork -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- 지정된 출력 파일 이름(소문자 -o)으로 SVG 이미지를 렌더링:

`patchwork -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- 출력을 PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON 또는 DOT 형식으로 렌더링:

`patchwork -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- `stdin` 및 `stdout`을 사용하여 `gif` 이미지 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | patchwork -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 도움말 표시:

`patchwork -?`
