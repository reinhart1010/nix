---
layout: page
title: common/pbmtobbnbg (한국어)
description: "PBM 이미지를 BitGraph 그래픽으로 변환."
content_hash: 612e408b34bdac97deb7659e7591ca557911593c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtobbnbg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtobbnbg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtobbnbg

PBM 이미지를 BitGraph 그래픽으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtobbnbg.html>.

- PBM 이미지를 BitGraph 터미널 Display Pixel Data 시퀀스로 변환:

`pbmtobbnbg < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.dpd</span>

- rasterop 지정:

`pbmtobbnbg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.dpd</span>
