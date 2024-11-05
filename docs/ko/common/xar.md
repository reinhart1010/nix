---
layout: page
title: common/xar (한국어)
description: ".xar 아카이브 관리."
content_hash: 847d4aa99370c47d0b0e9b8d9932cdc3c7f60294
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xar

.xar 아카이브 관리.
더 많은 정보: <https://manned.org/xar>.

- 주어진 디렉토리의 모든 파일로 xar 아카이브 생성:

`xar -cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.xar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 주어진 xar 아카이브의 내용 목록:

`xar -tf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.xar</span>

- 주어진 xar 아카이브의 내용을 현재 디렉토리로 추출:

`xar -xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.xar</span>
