---
layout: page
title: common/conda-create (한국어)
description: "새로운 conda 환경을 생성."
content_hash: 687e2c836c761b1e7fc7654025068b751bf88704
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/conda-create.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/conda-create.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/conda-create.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># conda create

새로운 conda 환경을 생성.
더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- `py39`라는 새로운 환경을 만들고, 여기에 Python 3.9 및 NumPy v1.11 이상을 설치:

`conda create --yes --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39</span>` python=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.9</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numpy>=1.11</span>`"`

- 환경의 완벽한 복사본 생성:

`conda create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39-copy</span>

- 지정된 이름으로 새 환경을 만들고 지정된 패키지를 설치:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
