---
layout: page
title: common/pnmcolormap (한국어)
description: "PNM 이미지에 대한 양자화 색상 맵 생성."
content_hash: 062e312d7a4953523945e54510dfcf2392ccbe2b
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pnmcolormap.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pnmcolormap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmcolormap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmcolormap

PNM 이미지에 대한 양자화 색상 맵 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- 입력 이미지와 최대한 유사하게 `n_colors` 이하의 색상만 사용하는 이미지 생성:

`pnmcolormap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 작은 디테일이 있는 이미지에 더 나은 결과를 제공할 수 있는 splitspread 전략 사용:

`pnmcolormap -splitspread `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 색상 맵을 정렬, 색상 맵 비교에 유용:

`pnmcolormap -sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
