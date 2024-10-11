---
layout: page
title: common/conda-install (한국어)
description: "기존 conda 환경에 패키지를 설치."
content_hash: ea0faa9f556fe767d8ca092baaa9852b20a51b64
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/conda-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/conda-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># conda install

기존 conda 환경에 패키지를 설치.
더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- 현재 활성 conda 환경에 하나 이상의 패키지를 설치:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 채널 conda-forge를 사용하여 현재 활성 conda 환경에 단일 패키지를 설치:

`conda install -c conda-forge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- conda-forge 채널을 사용하고 다른 채널을 무시하고 현재 활성 conda 환경에 단일 패키지를 설치:

`conda install -c conda-forge --override-channels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전의 패키지를 설치:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 특정 환경에 패키지를 설치:

`conda install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 현재 환경에서 패키지 업데이트:

`conda install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 메시지를 표시하지 않고 동의하여 패키지를 설치:

`conda install --yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
