---
layout: page
title: common/git-config (한국어)
description: "Git 저장소의 사용자 지정 설정 옵션을 관리합니다."
content_hash: 51deb94264e16e8e1f5c821f7895dbf8e89b2674
last_modified_at: 2024-08-19
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git config

Git 저장소의 사용자 지정 설정 옵션을 관리합니다.
이러한 설정은 개별 (현재 저장소) 또는 전역 (현재 사용자)용일 수 있습니다.
더 자세한 정보: <https://git-scm.com/docs/git-config>.

- 전역으로 이름이나 이메일을 설정 (이 정보는 저장소에 커밋하는 데 필요하며 모든 커밋에 포함):

`git config --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.name|user.email</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유저_이름|email@example.com</span>`"`

- 개별 저장소 또는 전역 설정 항목을 나열:

`git config --list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|global</span>

- 시스템 설정 항목만 나열하고(저장 위치: `/etc/gitconfig`), 파일 위치를 표시:

`git config --list --system --show-origin`

- 주어진 설정 항목의 값을 가져오기:

`git config alias.unstage`

- 주어진 설정 항목의 전역 값을 설정:

`git config --global alias.unstage "reset HEAD --"`

- 전역 설정 항목을 기본값으로 되돌리기:

`git config --global --unset alias.unstage`

- 개별 저장소의 Git 설정(`.git/config`)을 기본 편집기에서 편집:

`git config --edit`

- 전역 Git 설정(기본적으로 `~/.gitconfig` 또는 `$XDG_CONFIG_HOME/git/config` 파일이 존재하는 경우)을 기본 편집기에서 편집:

`git config --global --edit`
