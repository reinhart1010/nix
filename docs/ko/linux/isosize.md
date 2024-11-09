---
layout: page
title: linux/isosize (한국어)
description: "ISO 파일의 크기를 표시합니다."
content_hash: 925a05bbfd0593e824614e93bb3e6f86d0af0b05
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/isosize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/isosize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># isosize

ISO 파일의 크기를 표시합니다.
더 많은 정보: <https://manned.org/isosize>.

- ISO 파일의 크기 표시:

`isosize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>

- ISO 파일의 블록 수와 블록 크기 표시:

`isosize --sectors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>

- 주어진 수로 나눈 ISO 파일의 크기 표시 (--sectors 옵션이 없는 경우에만 사용 가능):

`isosize --divisor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>
