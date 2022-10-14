---
layout: page
title: common/git-am (한국어)
description: "패치 파일을 적용한다. 이메일로 커밋을 받을 때 유용함."
content_hash: cbe6ec5ba6c7c275a1ffbbb1a201275c62f1f7e9
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git am

패치 파일을 적용한다. 이메일로 커밋을 받을 때 유용함.
패치 파일을 생성 할 수 있는 `git format-patch` 또한 참고.
더 많은 정보: <https://git-scm.com/docs/git-am>.

- 패치 파일 적용:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.patch</span>

- 패치 파일 적용 프로세스 중단:

`git am --abort`

- 가능한 많은 수의 패치 파일 적용, 실패한 파일은 거절 파일에 저장:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.patch</span>
