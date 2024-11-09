---
layout: page
title: linux/pmount (한국어)
description: "일반 사용자가 임의의 핫플러그 가능 장치를 마운트."
content_hash: 931ab84750d3a703192f7a566f4fb2bfd8f620d9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pmount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pmount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pmount

일반 사용자가 임의의 핫플러그 가능 장치를 마운트.
더 많은 정보: <https://manned.org/pmount>.

- 장치를 `/media/` 아래에 마운트(장치를 마운트 지점으로 사용):

`pmount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/to/block/device</span>

- 특정 파일시스템 타입으로 장치를 `/media/label`에 마운트:

`pmount --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/to/block/device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨</span>

- CD-ROM을 읽기 전용 모드로 마운트(파일시스템 타입 ISO9660):

`pmount --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` --read-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- NTFS로 포맷된 디스크를 읽기-쓰기 모드로 강제 마운트:

`pmount --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` --read-write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 마운트된 모든 이동식 장치 표시:

`pmount`
