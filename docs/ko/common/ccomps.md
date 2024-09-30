---
layout: page
title: common/ccomps (한국어)
description: "그래프를 연결된 구성 요소로 분해."
content_hash: e481c6da6726c3e4b3281298fe1e0ae633a79173
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/ccomps.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ccomps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ccomps

그래프를 연결된 구성 요소로 분해.
그래프비즈 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://graphviz.org/pdf/ccomps.1.pdf>.

- 하나 이상의 그래프를 연결된 구성 요소로 분해:

`ccomps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>

- 하나 이상의 그래프에서 노드, 간선 및 연결된 구성요소의 수를 인쇄:

`ccomps -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일2.gv ...</span>

- `output.gv`를 기반으로 번호가 매겨진 파일이름에 연결된 각 구성요소를 작성:

`ccomps -x -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일2.gv ...</span>

- 도움말 표시:

`ccomps -?`
