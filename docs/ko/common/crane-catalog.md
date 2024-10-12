---
layout: page
title: common/crane-catalog (한국어)
description: "레지스트리의 저장소를 나열."
content_hash: a1ba459d38cf3f8892d89ca5a93a2bbed30adb41
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-catalog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-catalog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane catalog

레지스트리의 저장소를 나열.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_catalog.md>.

- 레지스트리의 저장소를 나열:

`crane catalog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_주소</span>

- 전체 이미지 참조를 출력:

`crane catalog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_주소</span>` --full-ref`

- 도움말 표시:

`crane catalog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
