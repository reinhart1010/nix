---
layout: page
title: common/idevicecrashreport (한국어)
description: "iOS 장치에서 충돌 보고서를 검색."
content_hash: b600486c814db3166185a58b6b02cc5d26d91081
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/idevicecrashreport.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/idevicecrashreport.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># idevicecrashreport

iOS 장치에서 충돌 보고서를 검색.
더 많은 정보: <https://manned.org/idevicecrashreport>.

- 충돌 보고서를 검색하여 지정된 디렉터리로 이동:

`idevicecrashreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 장치에서 충돌 보고서를 제거하지 않고 검색:

`idevicecrashreport --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 충돌 보고서를 별도의 `.crash` 파일로 추출:

`idevicecrashreport --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
