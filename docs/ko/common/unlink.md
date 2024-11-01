---
layout: page
title: common/unlink (한국어)
description: "파일 시스템에서 파일에 대한 링크를 제거."
content_hash: 0e740e6518ddd9bcbede0769db2b132a0cb9680b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/unlink.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unlink.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unlink.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unlink

파일 시스템에서 파일에 대한 링크를 제거.
해당 링크가 파일의 마지막 링크인 경우 파일 내용이 손실됩니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/unlink>.

- 지정된 파일이 마지막 링크인 경우 해당 파일 제거:

`unlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
