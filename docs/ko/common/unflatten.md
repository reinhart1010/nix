---
layout: page
title: common/unflatten (한국어)
description: "방향 그래프의 레이아웃 가로 세로 비율을 개선하기 위해 조정."
content_hash: 12db5540cd99f9c35d1a49524702398beb0591a6
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/unflatten.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unflatten.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unflatten.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unflatten

방향 그래프의 레이아웃 가로 세로 비율을 개선하기 위해 조정.
Graphviz 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://www.graphviz.org/pdf/unflatten.1.pdf>.

- 하나 이상의 방향 그래프를 조정하여 레이아웃 가로 세로 비율을 개선:

`unflatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.gv</span>

- `unflatten`을 `dot` 레이아웃 전처리기로 사용하여 가로 세로 비율 개선:

`unflatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>` | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 도움말 표시:

`unflatten -?`
