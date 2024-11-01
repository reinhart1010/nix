---
layout: page
title: common/znew (한국어)
description: "`.Z` 파일을 gzip 형식으로 다시 압축."
content_hash: a969d015028bf8dd0b187f742d52f0bbdd3a99be
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/znew.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/znew.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># znew

`.Z` 파일을 gzip 형식으로 다시 압축.
더 많은 정보: <https://manned.org/znew>.

- 파일을 `.Z`에서 gzip 형식으로 다시 압축:

`znew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z</span>

- 여러 파일을 다시 압축하고 각 파일의 크기 감소율을 표시:

`znew -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z 경로/대상/파일2.Z ...</span>

- 가장 느린 압축 방법을 사용하여 파일을 다시 압축 (최적의 압축을 위해):

`znew -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z</span>

- gzip 파일보다 작으면 `.Z` 파일을 [K]eeping하여 파일을 다시 압축:

`znew -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z</span>
