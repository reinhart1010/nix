---
layout: page
title: linux/grub-editenv (한국어)
description: "GRUB 환경 변수를 편집."
content_hash: d7e6f82e78c5575e554ccd11d38b2629fefa44db
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/grub-editenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grub-editenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grub-editenv

GRUB 환경 변수를 편집.
더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- 기본 부팅 항목 설정 (부팅 항목이 이미 존재한다고 가정):

`grub-editenv /boot/grub/grubenv set default=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ubuntu</span>

- `timeout` 변수의 현재 값 표시:

`grub-editenv /boot/grub/grubenv list timeout`

- `saved_entry` 변수를 기본값으로 재설정:

`grub-editenv /boot/grub/grubenv unset saved_entry`

- 커널 명령줄에 "quiet splash" 추가:

`grub-editenv /boot/grub/grubenv list kernel_cmdline`
