---
layout: page
title: common/bcomps (한국어)
description: "그래프를 이중 연결 구성 요소로 분해."
content_hash: 45a53755aa2cc333299a13fc1e03e802426e0df9
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bcomps.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bcomps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bcomps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bcomps

그래프를 이중 연결 구성 요소로 분해.
그래프비즈 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://graphviz.org/pdf/bcomps.1.pdf>.

- 하나 이상의 그래프를 이중 연결 구성요소로 분해:

`bcomps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.gv</span>

- 하나 이상의 그래프에서 블록 및 절단되는 정점 수를 인쇄:

`bcomps -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input2.gv ...</span>

- `output.gv`를 기반으로 각 블록과 블록-절단정점 트리를 여러 번호의 파일 이름에 쓰기:

`bcomps -x -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input1.gv 경로/대상/input2.gv ...</span>

- 도움말 표시:

`bcomps -?`
