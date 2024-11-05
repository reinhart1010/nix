---
layout: page
title: common/pamshadedrelief (한국어)
description: "고도 지도를 사용하여 음영 지형도를 생성."
content_hash: 11213309acd7c684559bdea29d77d93f0e3cd9e0
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamshadedrelief.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamshadedrelief.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamshadedrelief.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamshadedrelief

고도 지도를 사용하여 음영 지형도를 생성.
같이 보기: `pamcrater`, `ppmrelief`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

- 입력 이미지를 고도 지도로 해석하여 음영 지형도 이미지 생성:

`pamshadedrelief < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 지정된 계수로 이미지 감마 조정:

`pamshadedrelief -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계수</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
