---
layout: page
title: common/dot (한국어)
description: "방향 그래프의 레이어 도면을 생성하는 명령 도구입니다."
content_hash: 42cf6f5e0a332bb3f5d9d931594942169e90b70a
related_topics:
  - title: English version
    url: /en/common/dot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dot.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dot

방향 그래프의 레이어 도면을 생성하는 명령 도구입니다.
더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 선택한 포맷을 기반으로 이미지 파일을 랜더링하고 출력파일 이름 결정하기:

`dot -Tpng -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.dot</span>

- DOT 파일로부터 SVG 생성하기:

`dot -Tsvg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/출력_파일명.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.dot</span>
