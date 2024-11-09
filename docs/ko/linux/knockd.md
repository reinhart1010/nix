---
layout: page
title: linux/knockd (한국어)
description: "포트 노킹을 감지하고 스크립트를 실행하는 포트 노킹 데몬."
content_hash: 17803492f6ffd5742fe3a12771c8e29a8530e924
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/knockd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/knockd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># knockd

포트 노킹을 감지하고 스크립트를 실행하는 포트 노킹 데몬.
더 많은 정보: <https://manned.org/knockd>.

- knockd 시스템 데몬 시작:

`knockd -d`

- 지정된 구성 [f]파일을 사용하여 knockd 실행:

`knockd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.configuration`
