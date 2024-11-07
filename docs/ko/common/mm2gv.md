---
layout: page
title: common/mm2gv (한국어)
description: "그래프를 Matrix Market `mm` 형식에서 `gv` 형식으로 변환."
content_hash: b07d336ecb341bf5b7720510a21cf21a903abd4e
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mm2gv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mm2gv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mm2gv

그래프를 Matrix Market `mm` 형식에서 `gv` 형식으로 변환.
변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
더 많은 정보: <https://graphviz.org/pdf/mm2gv.1.pdf>.

- 그래프를 `mm` 형식에서 `gv` 형식으로 변환:

`mm2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mm</span>

- `stdin`과 `stdout`을 사용하여 그래프 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mm</span>` | mm2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gv</span>

- 도움말 표시:

`mm2gv -?`
