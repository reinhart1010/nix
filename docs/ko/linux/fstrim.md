---
layout: page
title: linux/fstrim (한국어)
description: "마운트된 파일 시스템에서 사용되지 않는 블록을 삭제합니다."
content_hash: 5cd6811af1824f30b8b10f844399f01e9fb0b9b6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fstrim.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fstrim.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fstrim

마운트된 파일 시스템에서 사용되지 않는 블록을 삭제합니다.
SSD 및 microSD 카드와 같은 플래시 메모리 장치에서만 지원됩니다.
더 많은 정보: <https://manned.org/fstrim>.

- 지원되는 모든 마운트된 파티션의 사용되지 않는 블록 삭제:

`sudo fstrim --all`

- 지정된 파티션의 사용되지 않는 블록 삭제:

`sudo fstrim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- 삭제 후 통계 표시:

`sudo fstrim --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>
