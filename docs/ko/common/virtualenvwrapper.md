---
layout: page
title: common/virtualenvwrapper (한국어)
description: "Python의 `virtualenv` 도구를 위한 간단한 래퍼 명령 그룹."
content_hash: 9aa459b35701a78e5e1f2ed640b170967ff94f7f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/virtualenvwrapper.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/virtualenvwrapper.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># virtualenvwrapper

Python의 `virtualenv` 도구를 위한 간단한 래퍼 명령 그룹.
더 많은 정보: <https://virtualenvwrapper.readthedocs.org>.

- 새로운 Python `virtualenv`를 `$WORKON_HOME`에 생성:

`mkvirtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 특정 Python 버전에 대한 `virtualenv` 생성:

`mkvirtualenv --python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local/bin/python3.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 다른 `virtualenv` 활성화 또는 사용:

`workon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- `virtualenv` 중지:

`deactivate`

- 모든 가상 환경 나열:

`lsvirtualenv`

- `virtualenv` 제거:

`rmvirtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 모든 virtualenvwrapper 명령 요약 보기:

`virtualenvwrapper`
