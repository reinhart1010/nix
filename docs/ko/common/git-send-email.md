---
layout: page
title: common/git-send-email (한국어)
description: "여러 개의 패치를 이메일로 전송."
content_hash: ac6b67be9fe452c3e9510c27552d6c8c3802444e
last_modified_at: 2024-10-07
related_topics:
  - title: Deutsch version
    url: /de/common/git-send-email.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-send-email.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-send-email.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-send-email.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-send-email.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git send-email

여러 개의 패치를 이메일로 전송.
패치는 파일, 디렉토리 또는 수정 목록으로 지정할 수 있습니다.
더 많은 정보: <https://git-scm.com/docs/git-send-email>.

- 현재 브랜치에서 마지막 커밋을 대화형으로 전송:

`git send-email -1`

- 지정된 커밋 전송:

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 현재 브랜치에서 여러 개의 커밋(예: 10개) 전송:

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- 패치 시리즈에 대한 소개 이메일 메시지 전송:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_수</span>` --compose`

- 전송할 각 패치의 이메일 메시지 검토 및 편집:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_수</span>` --annotate`
