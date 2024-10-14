---
layout: page
title: linux/mkfs.exfat (한국어)
description: "파티션 내에 exfat 파일 시스템 생성."
content_hash: 97f73a61556dbc8f736eb2aef23127658f774fa6
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/mkfs.exfat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.exfat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.exfat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.exfat

파티션 내에 exfat 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.exfat>.

- 장치 b의 파티션 1 (`sdb1`) 에 exfat 파일 시스템 생성:

`mkfs.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 이름을 지정하여 파일 시스템 생성:

`mkfs.exfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 ID를 지정하여 파일 시스템 생성:

`mkfs.exfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
