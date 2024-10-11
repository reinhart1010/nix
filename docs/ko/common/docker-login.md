---
layout: page
title: common/docker-login (한국어)
description: "Docker 레지스트리에 로그인."
content_hash: fa37f4a7aa4f0aefb2dac3787b5cdec8720376d2
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-login.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-login.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-login.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-login.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-login.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker login

Docker 레지스트리에 로그인.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/login/>.

- 레지스트리에 대화형으로 로그인:

`docker login`

- 특정 사용자 명으로 레지스트리에 로그인 (사용자는 비밀번호를 입력하라는 메시지를 받음):

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>

- 사용자 명과 비밀번호로 레지스트리에 로그인:

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>

- `stdin`에서 비밀번호를 받아 레지스트리에 로그인:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password-stdin`
