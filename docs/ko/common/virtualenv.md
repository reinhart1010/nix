---
layout: page
title: common/virtualenv (한국어)
description: "가상 격리된 Python 환경 생성."
content_hash: 5316f45849dc1a05b96023e8ef5261f11bc4014b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/virtualenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/virtualenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/virtualenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># virtualenv

가상 격리된 Python 환경 생성.
더 많은 정보: <https://virtualenv.pypa.io/>.

- 새 환경 생성:

`virtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/venv</span>

- 프롬프트 접두사를 사용자 정의:

`virtualenv --prompt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트_접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/venv</span>

- virtualenv에 다른 버전의 Python 사용:

`virtualenv --python=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pythonbin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/venv</span>

- 환경 시작(선택):

`source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/venv</span>`/bin/activate`

- 환경 중지:

`deactivate`
