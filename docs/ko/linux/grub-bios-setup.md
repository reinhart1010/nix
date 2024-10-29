---
layout: page
title: linux/grub-bios-setup (한국어)
description: "GRUB을 BIOS 구성으로 사용하는 장치 설정."
content_hash: 4b83800e6a1b1af88936cf453263b760fb4a8d25
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/grub-bios-setup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grub-bios-setup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grub-bios-setup

GRUB을 BIOS 구성으로 사용하는 장치 설정.
대부분의 경우 `grub-bios-setup` 대신 `grub-install`을 사용해야 합니다.
더 많은 정보: <https://manned.org/grub-bios-setup.8>.

- GRUB으로 부팅하도록 장치 설정:

`grub-bios-setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 문제가 감지되어도 설치 강행:

`grub-bios-setup --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 특정 디렉터리에 GRUB 설치:

`grub-bios-setup --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
