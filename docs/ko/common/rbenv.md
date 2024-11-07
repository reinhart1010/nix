---
layout: page
title: common/rbenv (한국어)
description: "쉽게 Ruby 버전을 설치하고 애플리케이션 환경을 관리."
content_hash: cb2eb07b0118ca29ee4717739c41f20a495b6b68
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rbenv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rbenv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rbenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rbenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rbenv

쉽게 Ruby 버전을 설치하고 애플리케이션 환경을 관리.
같이 보기: `asdf`.
더 많은 정보: <https://github.com/rbenv/rbenv>.

- Ruby 버전 설치:

`rbenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 각 Ruby의 최신 안정 버전 목록 표시:

`rbenv install --list`

- 설치된 Ruby 버전 목록 표시:

`rbenv versions`

- 시스템 전체에서 특정 Ruby 버전 사용:

`rbenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 애플리케이션/프로젝트 디렉토리에 특정 Ruby 버전 사용:

`rbenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 현재 선택된 Ruby 버전 표시:

`rbenv version`

- Ruby 버전 제거:

`rbenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 지정된 실행 파일을 포함하는 모든 Ruby 버전 표시:

`rbenv whence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>
