---
layout: page
title: linux/grubby (한국어)
description: "`grub` 및 `zipl` 부트로더를 설정하는 도구."
content_hash: 3c7f8744628f0f0bf2e4c37a0f89102ec2bb8cc5
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/grubby.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/grubby.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grubby.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grubby

`grub` 및 `zipl` 부트로더를 설정하는 도구.
더 많은 정보: <https://manned.org/grubby.8>.

- 모든 커널 메뉴 항목에 커널 부팅 인자 추가:

`sudo grubby --update-kernel=ALL --args '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet console=ttyS0</span>`'`

- 기본 커널 항목에서 기존 인자 제거:

`sudo grubby --update-kernel=DEFAULT --remove-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet</span>

- 모든 커널 메뉴 항목 나열:

`sudo grubby --info=ALL`
