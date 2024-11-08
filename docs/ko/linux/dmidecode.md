---
layout: page
title: linux/dmidecode (한국어)
description: "DMI(또는 SMBIOS로 알려진) 테이블의 내용을 사람이 읽을 수 있는 형식으로 표시합니다."
content_hash: b5f0fc99e6cf0a7ecb9fe1e32b1e88ec82d42758
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/dmidecode.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmidecode.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmidecode.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmidecode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dmidecode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmidecode

DMI(또는 SMBIOS로 알려진) 테이블의 내용을 사람이 읽을 수 있는 형식으로 표시합니다.
루트 권한이 필요합니다.
더 많은 정보: <https://manned.org/dmidecode>.

- 모든 DMI 테이블 내용을 표시:

`sudo dmidecode`

- BIOS 버전 표시:

`sudo dmidecode -s bios-version`

- 시스템의 일련번호 표시:

`sudo dmidecode -s system-serial-number`

- BIOS 정보 표시:

`sudo dmidecode -t bios`

- CPU 정보 표시:

`sudo dmidecode -t processor`

- 메모리 정보 표시:

`sudo dmidecode -t memory`
