---
layout: page
title: common/tred (한국어)
description: "방향 그래프의 전이 축소를 계산."
content_hash: 01ac4cfb6b55d5ecf76f5f5a1004cb9de10d083d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tred.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tred.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tred

방향 그래프의 전이 축소를 계산.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://www.graphviz.org/pdf/tred.1.pdf>.

- 하나 이상의 방향 그래프의 전이 축소 그래프 생성:

`tred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gv</span>

- 도움말 표시:

`tred -?`
