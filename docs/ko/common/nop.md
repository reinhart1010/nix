---
layout: page
title: common/nop (한국어)
description: "그래프의 유효성을 검사하고 정규 형식으로 예쁘게 출력."
content_hash: 75637fd2183b478401cfa8b82db18da2be8122a0
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nop

그래프의 유효성을 검사하고 정규 형식으로 예쁘게 출력.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://www.graphviz.org/pdf/nop.1.pdf>.

- 하나 이상의 그래프를 정규 형식으로 예쁘게 출력:

`nop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gv</span>

- 하나 이상의 그래프 유효성 검사, 출력 그래프는 생성하지 않음:

`nop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력2.gv ...</span>

- 도움말 표시:

`nop -?`
