---
layout: page
title: linux/gpasswd (한국어)
description: "`/etc/group` 및 `/etc/gshadow`를 관리합니다."
content_hash: 105f0d15708a2c39c3f19b1295a31512f0770a54
last_modified_at: 2024-11-11
related_topics:
  - title: العربية version
    url: /ar/linux/gpasswd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/gpasswd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gpasswd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpasswd

`/etc/group` 및 `/etc/gshadow`를 관리합니다.
더 많은 정보: <https://manned.org/gpasswd>.

- 그룹 관리자 정의:

`sudo gpasswd -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자1,사용자2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>

- 그룹 구성원 목록 설정:

`sudo gpasswd -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자1,사용자2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>

- 지정된 그룹에 비밀번호 생성:

`gpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>

- 지정된 그룹에 사용자 추가:

`gpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>

- 지정된 그룹에서 사용자 제거:

`gpasswd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>
