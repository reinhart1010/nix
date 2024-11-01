---
layout: page
title: common/zipinfo (한국어)
description: "Zip 파일의 내용에 대한 자세한 정보를 나열."
content_hash: 619658104146fed21f2518f6b94a62e6b5160d24
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zipinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipinfo

Zip 파일의 내용에 대한 자세한 정보를 나열.
더 많은 정보: <https://manned.org/zipinfo>.

- Zip 파일의 모든 파일을 긴 형식(권한, 소유권, 크기 및 수정 날짜)으로 나열:

`zipinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- Zip 파일의 모든 파일을 나열:

`zipinfo -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>
