---
layout: page
title: common/pngcrush (한국어)
description: "PNG 압축 유틸리티."
content_hash: 1ecc41346dcbcb04d69c8f24bf88f2cb491f2912
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pngcrush.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pngcrush.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pngcrush

PNG 압축 유틸리티.
더 많은 정보: <https://pmt.sourceforge.io/pngcrush>.

- PNG 파일 압축:

`pngcrush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.png</span>

- 모든 PNG 파일 압축 후 지정된 디렉토리에 출력:

`pngcrush -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>` *.png`

- 사용 가능한 모든 114개의 알고리즘으로 PNG 파일을 압축하고 최상의 결과 선택:

`pngcrush -rem allb -brute -reduce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.png</span>
