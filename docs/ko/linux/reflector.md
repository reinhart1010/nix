---
layout: page
title: linux/reflector (한국어)
description: "Arch 스크립트로 미러리스트를 가져오고 정렬합니다."
content_hash: 87ee16abbc13e2387039bf8f88f28c103c5feb87
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/reflector.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/reflector.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reflector

Arch 스크립트로 미러리스트를 가져오고 정렬합니다.
더 많은 정보: <https://manned.org/reflector>.

- 모든 미러를 가져와 다운로드 속도로 정렬하고 저장:

`sudo reflector --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rate</span>` --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- 독일의 HTTPS 미러만 가져오기:

`reflector --country `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>

- 최근에 동기화된 10개의 미러만 가져오기:

`reflector --latest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
