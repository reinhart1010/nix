---
layout: page
title: common/pyenv-virtualenv (한국어)
description: "설치된 Python 배포판을 기반으로 가상 환경을 생성합니다."
content_hash: a211baf83fc29e5c1bab00a635bb34cdbca32b35
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pyenv-virtualenv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/pyenv-virtualenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyenv virtualenv

설치된 Python 배포판을 기반으로 가상 환경을 생성합니다.
더 많은 정보: <https://github.com/pyenv/pyenv-virtualenv>.

- 새로운 Python 3.6.6 가상 환경 생성:

`pyenv virtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.6.6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 모든 기존 가상 환경 나열:

`pyenv virtualenvs`

- 가상 환경 활성화:

`pyenv activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 가상 환경 비활성화:

`pyenv deactivate`
