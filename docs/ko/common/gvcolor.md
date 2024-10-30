---
layout: page
title: common/gvcolor (한국어)
description: "다양한 색상으로 순위가 매겨진 이중 그래프를 색깔 입히기."
content_hash: 48edcb02a29915b7ad6afd924538a55fab286c13
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gvcolor.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gvcolor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gvcolor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gvcolor

다양한 색상으로 순위가 매겨진 이중 그래프를 색깔 입히기.
그래프비즈 필터: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
더 많은 정보: <https://graphviz.org/pdf/gvcolor.1.pdf>.

- 하나 이상의 순위가 매겨진 이중 그래프(이미 `dot`으로 처리됨)에 색상을 지정:

`gvcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레이아웃2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gv</span>

- 그래프를 배치하고 색상을 지정한 다음, PNG 이미지로 변환:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gv</span>` | gvcolor | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 도움말 표시:

`gvcolor -?`
