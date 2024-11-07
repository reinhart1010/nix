---
layout: page
title: common/runsvdir (한국어)
description: "전체 서비스 디렉터리를 실행."
content_hash: 78f7b9a3be1c7b99e52e196f6d3cbbe361bb95f6
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/runsvdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/runsvdir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/runsvdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># runsvdir

전체 서비스 디렉터리를 실행.
더 많은 정보: <https://manned.org/runsvdir.8>.

- 현재 사용자로 디렉터리 내 모든 서비스 시작 및 관리:

`runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>

- 루트 사용자로 디렉터리 내 모든 서비스 시작 및 관리:

`sudo runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>

- 개별 세션에서 서비스 시작:

`runsvdir -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스</span>
