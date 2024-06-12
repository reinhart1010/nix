---
layout: page
title: common/git-rm (한국어)
description: "저장소 인덱스와 로컬 파일 시스템에서 파일을 제거합니다."
content_hash: 88b448d6d76e7153d2e191091bece6a2eb8bfa21
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git rm

저장소 인덱스와 로컬 파일 시스템에서 파일을 제거합니다.
더 많은 정보: <https://git-scm.com/docs/git-rm>.

- 저장소 인덱스와 파일 시스템에서 파일 제거:

`git rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉토리 제거:

`git rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 저장소 인덱스에서 파일 제거하되 로컬에서는 그대로 유지:

`git rm --cached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
