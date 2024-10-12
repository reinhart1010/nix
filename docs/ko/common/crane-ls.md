---
layout: page
title: common/crane-ls (한국어)
description: "저장소의 태그를 나열."
content_hash: 1befeea875a48878c031400256da77415282e59b
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane ls

저장소의 태그를 나열.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_ls.md>.

- 태그 나열:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>

- 전체 이미지 참조 출력:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>` --full-ref`

- 다이제스트 태그 생략:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--omit-digest-tags</span>

- 도움말 표시:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
