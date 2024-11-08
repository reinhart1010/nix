---
layout: page
title: common/mingle (한국어)
description: "그래프 레이아웃의 엣지를 번들링."
content_hash: 210629b988b470ae2dc89d178652c34f32204985
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mingle.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mingle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mingle

그래프 레이아웃의 엣지를 번들링.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://www.graphviz.org/pdf/mingle.1.pdf>.

- 하나 이상의 그래프 레이아웃(이미 레이아웃 정보가 있는)의 엣지를 번들링:

`mingle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gv</span>

- 레이아웃, 번들링을 수행하고 한 번의 명령으로 그림으로 출력:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>` | mingle | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 도움말 표시:

`mingle -?`
