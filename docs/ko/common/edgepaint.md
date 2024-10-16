---
layout: page
title: common/edgepaint (한국어)
description: "교차하는 가장자리를 명확하게 하기 위해, 그래프 레이아웃의 가장자리에 색상을 지정."
content_hash: 26a915a77fa362d204393df58a92543f66b4cf60
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/edgepaint.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/edgepaint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/edgepaint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># edgepaint

교차하는 가장자리를 명확하게 하기 위해, 그래프 레이아웃의 가장자리에 색상을 지정.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://graphviz.org/pdf/edgepaint.1.pdf>.

- 하나 이상의 그래프 레이아웃 (이미 레이아웃 정보가 있음)의 가장자리에 색상을 지정하여, 교차하는 가장자리를 명확하게 함:

`edgepaint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 색 구성표를 사용하여 가장자리에 색상을 지정. (<https://graphviz.org/doc/info/colors.html#brewer> 참조):

`edgepaint -color-scheme=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accent7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 그래프를 배치하고 가장자리에 색상을 지정한다음, PNG 이미지로 변환:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gv</span>` | edgepaint | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.png</span>

- 도움말 표시:

`edgepaint -?`
