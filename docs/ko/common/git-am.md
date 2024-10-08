---
layout: page
title: common/git-am (한국어)
description: "패치 파일을 적용하고 커밋 생성. 이메일을 통해 커밋을 받을 때 유용합니다."
content_hash: 71198557dc0b9d1a4f85a05fb555d079096cb8f2
last_modified_at: 2024-10-08
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
  - title: Indonesia version
    url: /id/common/git-am.html
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
tldri18n_status: 2
---
# git am

패치 파일을 적용하고 커밋 생성. 이메일을 통해 커밋을 받을 때 유용합니다.
패치 파일을 생성할 수 있는 `git format-patch`도 같이 보세요.
더 많은 정보: <https://git-scm.com/docs/git-am>.

- 로컬 패치 파일을 적용하고 커밋:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.patch</span>

- 원격 패치 파일을 적용하고 커밋:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- 패치 파일 적용 과정 중단:

`git am --abort`

- 가능한 한 많은 패치 파일을 적용하고, 실패한 부분을 거부 파일로 저장:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.patch</span>
