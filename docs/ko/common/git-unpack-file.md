---
layout: page
title: common/git-unpack-file (한국어)
description: "Blob의 내용을 가진 임시 파일을 생성."
content_hash: e20e7cfa9a392da5f9c138e99ebfc912b3a2c4ce
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-unpack-file.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-unpack-file.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git unpack-file

Blob의 내용을 가진 임시 파일을 생성.
더 많은 정보: <https://git-scm.com/docs/git-unpack-file>.

- ID로 지정된 Blob의 내용을 가진 파일을 생성하고 임시 파일의 이름 출력:

`git unpack-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blob_id</span>
