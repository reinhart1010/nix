---
layout: page
title: linux/mkfs.btrfs (한국어)
description: "BTRFS 파일 시스템 생성."
content_hash: 3df6223ee0c4c8af7dd71b91a3cdbd27953880d1
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.btrfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.btrfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.btrfs

BTRFS 파일 시스템 생성.
기본값은 `raid1`로, 데이터 블록의 두 복사본이 두 개의 다른 장치에 분산됩니다.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- 단일 장치에 btrfs 파일 시스템 생성:

`sudo mkfs.btrfs --metadata single --data single `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 여러 장치에 raid1으로 btrfs 파일 시스템 생성:

`sudo mkfs.btrfs --metadata raid1 --data raid1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>

- 파일 시스템에 레이블 설정:

`sudo mkfs.btrfs --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>`]`
