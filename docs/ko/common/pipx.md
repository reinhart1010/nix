---
layout: page
title: common/pipx (한국어)
description: "Python 애플리케이션을 격리된 환경에서 설치하고 실행."
content_hash: 18cf06f455ddab5dd6370e235dd14b82f8e32d93
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pipx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pipx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pipx

Python 애플리케이션을 격리된 환경에서 설치하고 실행.
더 많은 정보: <https://github.com/pypa/pipx>.

- 임시 가상 환경에서 앱 실행:

`pipx run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pycowsay</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">moo</span>

- 가상 환경에 패키지 설치 및 진입점을 경로에 추가:

`pipx install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 나열:

`pipx list`

- 실행 파일과 다른 패키지 이름으로 임시 가상 환경에서 앱 실행:

`pipx run --spec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpx-cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpx</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.github.com</span>

- 기존 가상 환경에 의존성 추가:

`pipx inject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성1 의존성2 ...</span>

- pip 인자를 사용하여 가상 환경에 패키지 설치:

`pipx install --pip-args='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pip-인자</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 설치된 패키지 업그레이드/재설치/제거:

`pipx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upgrade-all|uninstall-all|reinstall-all</span>
