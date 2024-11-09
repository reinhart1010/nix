---
layout: page
title: linux/openrc (한국어)
description: "OpenRC 서비스 관리자."
content_hash: f149d0a01287e895bc2a7f2ba2d2d2cc874e537a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/openrc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/openrc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openrc

OpenRC 서비스 관리자.
같이 보기: `rc-status`, `rc-update`, `rc-service`.
더 많은 정보: <https://wiki.gentoo.org/wiki/OpenRC>.

- 특정 런레벨로 변경:

`sudo openrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런레벨_이름</span>

- 기존 서비스를 중지하지 않고 특정 런레벨로 변경:

`sudo openrc --no-stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런레벨_이름</span>
