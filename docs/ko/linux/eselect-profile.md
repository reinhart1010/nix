---
layout: page
title: linux/eselect-profile (한국어)
description: "시스템 프로필을 설정하는 `/etc/portage/make.profile` 심볼릭 링크를 관리하는 `eselect` 모듈."
content_hash: f551f2a06dbc436c36fce0b91c64cb6870a92c70
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/eselect-profile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-profile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect profile

시스템 프로필을 설정하는 `/etc/portage/make.profile` 심볼릭 링크를 관리하는 `eselect` 모듈.
더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- 사용 가능한 프로필 심볼릭 링크 대상과 그 번호 나열:

`eselect profile list`

- `list` 명령어의 이름 또는 번호로 `/etc/portage/make.profile` 심볼릭 링크 설정:

`eselect profile set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|번호</span>

- 현재 시스템 프로필 표시:

`eselect profile show`
