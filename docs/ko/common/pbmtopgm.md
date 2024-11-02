---
layout: page
title: common/pbmtopgm (한국어)
description: "PBM 이미지를 개별 픽셀 주변 영역의 평균을 내어 PGM으로 변환."
content_hash: d6188a8956e57748672e49d9614efd94ca004c89
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtopgm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtopgm

PBM 이미지를 개별 픽셀 주변 영역의 평균을 내어 PGM으로 변환.
같이 보기: `pnmconvol`, `pamditherbw`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtopgm.html>.

- 각 픽셀 주변의 `w`x`h` 크기 영역을 평균 내어 PBM 이미지를 PGM으로 변환:

`pbmtopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">w</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>
