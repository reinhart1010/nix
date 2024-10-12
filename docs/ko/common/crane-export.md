---
layout: page
title: common/crane-export (한국어)
description: "컨테이너 이미지의 파일 시스템을 tarball로 내보냄."
content_hash: 888aff2d17c00471288f6d0f2df5295be09b2f59
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-export.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-export.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane export

컨테이너 이미지의 파일 시스템을 tarball로 내보냄.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- stdout에 tarball을 작성 :

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` -`

- 파일에 tarball 쓰기:

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>

- stdin에서 이미지 읽기:

`crane export - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>
