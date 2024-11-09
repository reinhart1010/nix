---
layout: page
title: linux/fatlabel (한국어)
description: "FAT32 파티션의 레이블을 가져오거나 설정."
content_hash: fed1ac851865a951316907f0150baa66652bb450
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fatlabel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/fatlabel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fatlabel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fatlabel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fatlabel

FAT32 파티션의 레이블을 가져오거나 설정.
더 많은 정보: <https://manned.org/fatlabel>.

- FAT32 파티션의 레이블 가져오기:

`fatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- FAT32 파티션의 레이블 설정:

`fatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdc3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_레이블</span>`"`
