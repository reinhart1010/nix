---
layout: page
title: common/git (한국어)
description: "분산 버전 관리 시스템."
content_hash: 6c68acd256e2a38ae5ee764dee3122e51c2e7eef
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/git.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git

분산 버전 관리 시스템.
`commit`, `add`, `branch`, `checkout`, `push` 등의 특정 하위 명령어는 고유의 문서가 따로 있습니다. `tldr git subcommand`를 통해 확인할 수 있습니다.
더 많은 정보: <https://git-scm.com/>.

- 하위 명령어 실행:

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령어</span>

- 특정 레파지토리 위치에서 Git 하위 명령어 실행:

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">특정/레파지토리/경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령어</span>

- 주어진 설정으로 Git 하위 명령어 실행:

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정.키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정.값</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령어</span>

- 일반 도움말 출력:

`git --help`

- 하위 명령어 도움말 출력 (`clone`, `add`, `push`, `log`, 등등):

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명렁어</span>

- Git 버전 확인:

`git --version`
