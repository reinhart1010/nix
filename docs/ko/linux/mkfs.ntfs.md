---
layout: page
title: linux/mkfs.ntfs (한국어)
description: "파티션 내에 NTFS 파일 시스템 생성."
content_hash: 1b21a53a6a929caa3f4c1fd71e151525e2e3cec7
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/mkfs.ntfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.ntfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.ntfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.ntfs

파티션 내에 NTFS 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.ntfs>.

- 장치 b의 파티션 1 (`sdb1`) 에 NTFS 파일 시스템 생성:

`mkfs.ntfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 레이블을 지정하여 파일 시스템 생성:

`mkfs.ntfs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 특정 UUID로 파일 시스템 생성:

`mkfs.ntfs -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
