---
layout: page
title: common/pamcrater (한국어)
description: "분화구가 있는 지형의 PAM 이미지를 생성합니다."
content_hash: c5eb9c2e5af7a54b371f453b459a272ebd5cd2ad
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamcrater.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamcrater.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamcrater.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamcrater

분화구가 있는 지형의 PAM 이미지를 생성합니다.
같이 보기: `pamshadedrelief`, `ppmrelief`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamcrater.html>.

- 지정된 크기의 분화구 지형 이미지를 생성:

`pamcrater -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 지정된 개수의 분화구를 포함한 이미지 생성:

`pamcrater -number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분화구_개수</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
