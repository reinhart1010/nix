---
layout: page
title: common/ouch (한국어)
description: "파일 및 디렉터리를 압축하고 해제하는 명령줄 유틸리티."
content_hash: 7fbed579c3dbf07ca5c8fb891d0faf8824c83956
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ouch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ouch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ouch

파일 및 디렉터리를 압축하고 해제하는 명령줄 유틸리티.
더 많은 정보: <https://crates.io/crates/ouch>.

- 특정 파일 압축 해제:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.tar.xz</span>

- 특정 위치에 파일 압축 해제:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.tar.xz</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 여러 파일 압축 해제:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.tar 경로/대상/아카이브2.tar.gz ...</span>

- 파일 압축:

`ouch compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>
