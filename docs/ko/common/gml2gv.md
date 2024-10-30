---
layout: page
title: common/gml2gv (한국어)
description: "그래프를 `gml`에서 `gv` 형식으로 변환."
content_hash: e15b8f054e67515bf824e2d15559e202e6039ad0
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gml2gv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gml2gv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gml2gv

그래프를 `gml`에서 `gv` 형식으로 변환.
변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
더 많은 정보: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- 그래프를 `gml`에서 `gv` 형식으로 변환:

`gml2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력파일.gml</span>

- `stdin` 및 `stdout`을 사용하여 그래프를 반환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력파일.gml</span>` | gml2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- 도움말 표시:

`gml2gv -?`
