---
layout: page
title: common/gv2gxl (한국어)
description: "그래프를 `gv`에서 `gxl` 형식으로 변환."
content_hash: bb32b08e909608afbdec383faac2812d34dcf611
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gv2gxl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gv2gxl

그래프를 `gv`에서 `gxl` 형식으로 변환.
변환기: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
더 많은 정보: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- 그래프를 `gv`에서 `gxl` 형식으로 변환:

`gv2gxl -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gxl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.gv</span>

- `stdin` 및 `stdout`을 사용하여 그래프를 반환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.gv</span>` | gv2gxl > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.gxl</span>

- 도움말 표시:

`gv2gxl -?`
