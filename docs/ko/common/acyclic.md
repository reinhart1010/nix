---
layout: page
title: common/acyclic (한국어)
description: "일부 간선을 반전시켜 방향성 그래프를 순환이 없는 그래프로 변환합니다."
content_hash: 9f1a8f08bc9b61e2bfa8901d5a3bda2f71bf2345
last_modified_at: 2023-12-05
related_topics:
  - title: English version
    url: /en/common/acyclic.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acyclic.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acyclic.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acyclic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acyclic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acyclic

일부 간선을 반전시켜 방향성 그래프를 순환이 없는 그래프로 변환합니다.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://graphviz.org/pdf/acyclic.1.pdf>.

- 일부 간선을 반전시켜 방향성 그래프를 순환이 없는 그래프로 변환:

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gv</span>

- 그래프가 순환이 없거나 주기가 있거나 방향이 지정되지 않아 출력 그래프가 생성되지 않는 경우 출력:

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>

- `acyclic`의 도움말 표시:

`acyclic -?`
