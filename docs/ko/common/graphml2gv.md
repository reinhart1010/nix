---
layout: page
title: common/graphml2gv (한국어)
description: "그래프를 `graphml`에서 `gv` 형식으로 변환."
content_hash: 6623a10af43afbc5e9c011490ce73b8ea6ef4825
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/graphml2gv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# graphml2gv

그래프를 `graphml`에서 `gv` 형식으로 변환.
변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
더 많은 정보: <https://graphviz.org/pdf/graphml2gv.1.pdf>.

- 그래프를 `gml`에서 `gv` 형식으로 변환:

`graphml2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>

- `stdin` 및 `stdout`을 사용하여 그래프를 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>` | graphml2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gv</span>

- 도움말 표시:

`graphml2gv -?`
