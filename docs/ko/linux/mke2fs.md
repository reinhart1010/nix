---
layout: page
title: linux/mke2fs (한국어)
description: "파티션 내에 Linux 파일 시스템 생성."
content_hash: d35550a637b72b5266ad0488fe29421a94d8c5fc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mke2fs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mke2fs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mke2fs

파티션 내에 Linux 파일 시스템 생성.
더 많은 정보: <https://manned.org/mke2fs>.

- 장치 b의 파티션 1(`sdb1`)에 ext2 파일 시스템 생성:

`mkfs.ext2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 장치 b의 파티션 1(`sdb1`)에 ext3 파일 시스템 생성:

`mkfs.ext3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 장치 b의 파티션 1(`sdb1`)에 ext4 파일 시스템 생성:

`mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
