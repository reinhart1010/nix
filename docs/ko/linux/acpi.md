---
layout: page
title: linux/acpi (한국어)
description: "배터리 상태 또는 온도 정보를 표시합니다."
content_hash: 8898ac1497a1553d78839bb6371f34ee346d2787
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/acpi.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/acpi.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/acpi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/acpi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># acpi

배터리 상태 또는 온도 정보를 표시합니다.
더 많은 정보: <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- 배터리 정보 표시:

`acpi`

- 온도 정보 표시:

`acpi -t`

- 냉각 장치 정보 표시:

`acpi -c`

- 화씨로 온도 정보 표시:

`acpi -tf`

- 모든 정보 표시:

`acpi -V`

- `/sys` 대신 `/proc`에서 정보 추출:

`acpi -p`
