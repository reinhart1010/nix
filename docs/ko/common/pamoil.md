---
layout: page
title: common/pamoil (한국어)
description: "PAM 이미지를 유화로 변환."
content_hash: 00f824d9575973d87e71a98010b77652468be09c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamoil.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamoil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamoil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamoil

PAM 이미지를 유화로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamoil.html>.

- PAM 이미지를 유화로 변환:

`pamoil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pam</span>

- "번지기" 효과를 위해 N 픽셀의 이웃을 고려:

`pamoil -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pam</span>
