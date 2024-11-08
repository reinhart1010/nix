---
layout: page
title: linux/dkms (한국어)
description: "커널 모듈의 동적 빌드를 위한 프레임워크."
content_hash: bf1444736adf94b0b2096fb4dc17c5a97acd1026
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dkms.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dkms.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dkms.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dkms

커널 모듈의 동적 빌드를 위한 프레임워크.
더 많은 정보: <https://github.com/dell/dkms>.

- 현재 설치된 모듈 나열:

`dkms status`

- 현재 실행 중인 커널에 대해 모든 모듈 다시 빌드:

`dkms autoinstall`

- 현재 실행 중인 커널에 대해 acpi_call 모듈의 버전 1.2.1 설치:

`dkms install -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acpi_call</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.1</span>

- 모든 커널에서 acpi_call 모듈의 버전 1.2.1 제거:

`dkms remove -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acpi_call</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.1</span>` --all`
