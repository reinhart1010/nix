---
layout: page
title: common/sccmap (한국어)
description: "방향 그래프의 강하게 연결된 컴포넌트를 추출합니다."
content_hash: 482c35933aa9702334e93d9b141fcdf2552ef5f1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sccmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/sccmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sccmap

방향 그래프의 강하게 연결된 컴포넌트를 추출합니다.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://www.graphviz.org/pdf/sccmap.1.pdf>.

- 하나 이상의 방향 그래프에서 강하게 연결된 컴포넌트 추출:

`sccmap -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gv</span>

- 그래프에 대한 통계를 출력하며, 그래프 출력은 생성하지 않음:

`sccmap -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력2.gv ...</span>

- 도움말 표시:

`sccmap -?`
