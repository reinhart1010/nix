---
layout: page
title: common/gvpack (한국어)
description: "여러 그래프 레이아웃 (이미 레이아웃 정보가 있음을 결합)을 결합."
content_hash: 9cbba855ab43e4db375808422cfc02de368d7215
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gvpack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gvpack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gvpack

여러 그래프 레이아웃 (이미 레이아웃 정보가 있음을 결합)을 결합.
그래프비즈 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://graphviz.org/pdf/gvpack.1.pdf>.

- 이미 레이아웃 정보가 있는 여러 그래프 레이아웃을 결합:

`gvpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 그래프 수준에서 여러 그래프 레이아웃을 결합하여, 그래프를 별도로 유지:

`gvpack -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 클러스터를 무시하고, 노드 수준에서 여러 그래프 레이아웃을 결합:

`gvpack -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 패킹 없이 여러 그래프 레이아웃 결합:

`gvpack -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 도움말 표시:

`gvpack -?`
