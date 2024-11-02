---
layout: page
title: common/pyenv (한국어)
description: "여러 버전의 Python 사이를 쉽게 전환."
content_hash: 9aae065a3cd76227427f79e1f2ca4c6cd6cf9071
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pyenv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/pyenv.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/pyenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pyenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pyenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pyenv

여러 버전의 Python 사이를 쉽게 전환.
같이 보기: `asdf`.
더 많은 정보: <https://github.com/pyenv/pyenv>.

- 사용 가능한 모든 명령 나열:

`pyenv commands`

- `${PYENV_ROOT}/versions` 디렉토리 아래의 모든 Python 버전 나열:

`pyenv versions`

- 업스트림에서 설치할 수 있는 모든 Python 버전 나열:

`pyenv install --list`

- `${PYENV_ROOT}/versions` 디렉토리에 특정 Python 버전 설치:

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- `${PYENV_ROOT}/versions` 디렉토리에서 특정 Python 버전 제거:

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 현재 컴퓨터에서 전역으로 사용할 Python 버전 설정:

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 현재 디렉토리와 하위 디렉토리에서 사용할 Python 버전 설정:

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
