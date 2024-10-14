---
layout: page
title: linux/mkfs.bcachefs (한국어)
description: "파티션 내에 `bcachefs` 파일 시스템 생성."
content_hash: f18ecef3c3bbe1f039a6431e8f8d4294a603c465
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/mkfs.bcachefs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.bcachefs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.bcachefs

파티션 내에 `bcachefs` 파일 시스템 생성.
더 많은 정보: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- 장치 (`X`) 의 파티션 1에 `bcachefs` 파일 시스템 생성:

`sudo mkfs.bcachefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>

- 볼륨 레이블을 사용하여 `bcachefs` 파일 시스템 생성:

`sudo mkfs.bcachefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--fs_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>
