---
layout: page
title: common/ppmdist (한국어)
description: "PPM 이미지를 그레이스케일 버전으로 변환."
content_hash: c72fdd45917fffd891d1167d2eb240bc3502c7e1
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmdist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmdist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmdist

PPM 이미지를 그레이스케일 버전으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmdist.html>.

- 지정된 PPM 이미지의 그레이스케일 버전 생성:

`ppmdist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 지정된 방법을 사용하여 색상을 그레이 레벨로 매핑:

`ppmdist -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequency|intensity</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>
