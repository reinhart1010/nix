---
layout: page
title: common/pip3 (한국어)
description: "Python 패키지 관리자."
content_hash: 40a1e8db45dd36adcaaaf562713497cd8c873efe
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pip3.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip3.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip3.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pip3.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pip3

Python 패키지 관리자.
더 많은 정보: <https://pip.pypa.io>.

- 패키지 설치:

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전의 패키지 설치:

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 패키지 업그레이드:

`pip3 install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`pip3 uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 목록을 파일에 저장:

`pip3 freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- 파일에서 패키지 설치:

`pip3 install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- 설치된 패키지 정보 표시:

`pip3 show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
