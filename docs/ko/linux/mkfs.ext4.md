---
layout: page
title: linux/mkfs.ext4 (한국어)
description: "파티션 내에 ext4 파일 시스템 생성."
content_hash: f5bbcf6e3fd8d4408dea03dea9435f851fb1d313
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.ext4.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.ext4.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.ext4

파티션 내에 ext4 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.ext4>.

- 장치 b의 파티션 1 (`sdb1`) 에 ext4 파일 시스템 생성:

`sudo mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 라벨을 지정하여 ext4 파일 시스템 생성:

`sudo mkfs.ext4 -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_라벨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
