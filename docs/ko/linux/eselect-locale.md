---
layout: page
title: linux/eselect-locale (한국어)
description: "시스템 언어를 설정하는 `LANG` 환경 변수를 관리하기 위한 `eselect` 모듈."
content_hash: 47cc84ecb79d9e37e1327e01960e841d75e92c66
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/eselect-locale.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/eselect-locale.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-locale.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect locale

시스템 언어를 설정하는 `LANG` 환경 변수를 관리하기 위한 `eselect` 모듈.
더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- 사용 가능한 로케일 나열:

`eselect locale list`

- `list` 명령의 이름이나 인덱스로 `/etc/profile.env`에 `LANG` 환경 변수 설정:

`eselect locale set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|인덱스</span>

- `/etc/profile.env`의 `LANG` 값 표시:

`eselect locale show`
