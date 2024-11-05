---
layout: page
title: common/neato (한국어)
description: "`graphviz` 파일에서 `선형 무방향` 네트워크 그래프의 이미지를 렌더링."
content_hash: 32da18d97cb7bd9952608fc54dce82fadb05f552
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/neato.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/neato.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># neato

`graphviz` 파일에서 `선형 무방향` 네트워크 그래프의 이미지를 렌더링.
레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage`, `patchwork`.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 출력 형식에 기반하여 PNG 이미지 렌더링 (대문자 -O 사용):

`neato -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- 지정된 출력 파일 이름으로 SVG 이미지 렌더링 (소문자 -o 사용):

`neato -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, 또는 DOT 형식으로 출력 렌더링:

`neato -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- `stdin`과 `stdout`을 사용하여 GIF 이미지 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">graph {this -- that} </span>`" | neato -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 도움말 표시:

`neato -?`
