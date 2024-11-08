---
layout: page
title: linux/blkid (한국어)
description: "인식된 모든 파티션과 그에 대한 범용 고유 식별자(UUID)를 나열합니다."
content_hash: 7f85137b01c312f7cba886e9cb6555ecb54945ed
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/blkid.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/blkid.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/blkid.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/blkid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/blkid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># blkid

인식된 모든 파티션과 그에 대한 범용 고유 식별자(UUID)를 나열합니다.
더 많은 정보: <https://manned.org/blkid>.

- 모든 파티션 나열:

`sudo blkid`

- 현재 마운트 지점을 포함하여 테이블 형식으로 모든 파티션 나열:

`sudo blkid -o list`
