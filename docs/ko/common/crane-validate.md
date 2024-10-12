---
layout: page
title: common/crane-validate (한국어)
description: "이미지의 형식이 올바른지 확인."
content_hash: bd25f7adce1a43e7a27709abe68f447faddc1419
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-validate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-validate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane validate

이미지의 형식이 올바른지 확인.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- 이미지 유효성 검사:

`crane validate`

- 레이어 다운로드/다이제스트 건너뛰기:

`crane validate --fast`

- 유효성을 검사할 원격 이미지의 이름:

`crane validate --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>

- 유효성을 검사할 tarball 경로:

`crane validate --tarball `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>

- 도움말 표시:

`crane validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
