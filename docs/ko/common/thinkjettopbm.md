---
layout: page
title: common/thinkjettopbm (한국어)
description: "HP ThinkJet 프린터 명령 파일을 PBM 파일로 변환."
content_hash: 5e8602b02e90fa34d951f0fd15aaa89311f15b1e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/thinkjettopbm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/thinkjettopbm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># thinkjettopbm

HP ThinkJet 프린터 명령 파일을 PBM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/thinkjettopbm.html>.

- HP ThinkJet 프린터 명령 파일을 PBM 파일로 변환:

`thinkjettopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 디버그 정보를 `stderr`에 출력:

`thinkjettopbm -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
