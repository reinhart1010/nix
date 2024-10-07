---
layout: page
title: common/git-request-pull (한국어)
description: "업스트림 프로젝트에 변경 사항을 병합해 달라고 요청하는 요청서를 생성."
content_hash: d949addb8a29adb8f2f116a5148897196353bc9e
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-request-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-request-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-request-pull.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-request-pull.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git request-pull

업스트림 프로젝트에 변경 사항을 병합해 달라고 요청하는 요청서를 생성.
더 많은 정보: <https://git-scm.com/docs/git-request-pull>.

- v1.1 릴리스와 지정된 브랜치 간의 변경 사항을 요약한 요청서 생성:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- `foo` 브랜치의 v0.1 릴리스와 로컬 `bar` 브랜치 간의 변경 사항을 요약한 요청서 생성:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo:bar</span>
