---
layout: page
title: common/zint (한국어)
description: "바코드 및 QR 코드를 생성."
content_hash: b580d1a43046c55b2326de4dd251a2035b31d35c
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zint.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zint

바코드 및 QR 코드를 생성.
더 많은 정보: <https://www.zint.org.uk/manual/chapter/4>.

- 바코드를 생성하고 저장:

`zint --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8 데이터</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 생성할 코드 유형 지정:

`zint --barcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드_유형</span>` --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8 데이터</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지원되는 모든 코드 유형 나열:

`zint --types`
