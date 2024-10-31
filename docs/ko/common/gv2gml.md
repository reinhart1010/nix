---
layout: page
title: common/gv2gml (한국어)
description: "그래프를 `gv`에서 `gml`형식으로 변환."
content_hash: b729f6ca91149d7543621cd3d1eda8738688936c
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gv2gml.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gv2gml

그래프를 `gv`에서 `gml`형식으로 변환.
변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
더 많은 정보: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- 그래프를 `gv`에서 `gml`형식으로 변환.:

`gv2gml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>

- `stdin` 및 `stdout` 사용하여 그래프를 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.gv</span>` | gv2gml > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gml</span>

- 도움말 표시:

`gv2gml -?`
