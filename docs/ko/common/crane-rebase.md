---
layout: page
title: common/crane-rebase (한국어)
description: "이미지를 새로운 기본 이미지로 rebase."
content_hash: 71c69294b52385ea71d8aeec2ec06bae52aec471
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-rebase.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-rebase.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane rebase

이미지를 새로운 기본 이미지로 rebase.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- 이미지 rebase:

`crane rebase`

- 새로운 기본 이미지 삽입:

`crane rebase --new_base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>

- 오래된 이미지 제거:

`crane rebase --old_base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>

- rebase된 이미지에 적용할 태그 추가:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 도움말 표시:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
