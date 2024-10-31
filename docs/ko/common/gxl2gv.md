---
layout: page
title: common/gxl2gv (한국어)
description: "그래프를 `gxl`에서 `gv` 형식으로 변환."
content_hash: 6321db79110bc186a8fd00b99b9d27b64729e13a
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gxl2gv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gxl2gv

그래프를 `gxl`에서 `gv` 형식으로 변환.
변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
더 많은 정보: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- 그래프를 `gxl`에서 `gv` 형식으로 변환:

`gxl2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.gxl</span>

- `stdin` 및 `stdout`을 사용하여 그래프를 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.gxl</span>` | gxl2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gv</span>

- 도움말 표시:

`gxl2gv -?`
