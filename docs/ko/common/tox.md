---
layout: page
title: common/tox (한국어)
description: "여러 Python 버전에서 Python 테스트를 자동화."
content_hash: 054f80a8d7fd5392920777e2aedf49c7452862c9
last_modified_at: 2024-11-10
related_topics:
  - title: العربية version
    url: /ar/common/tox.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tox.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tox

여러 Python 버전에서 Python 테스트를 자동화.
tox.ini를 사용하여 환경 및 테스트 명령을 구성하세요.
더 많은 정보: <https://github.com/tox-dev/tox>.

- 모든 테스트 환경에서 테스트 실행:

`tox`

- `tox.ini` 구성 생성:

`tox-quickstart`

- 사용 가능한 환경 나열:

`tox --listenvs-all`

- 특정 환경에서 테스트 실행 (예: Python 3.6):

`tox -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py36</span>

- 가상 환경을 강제로 재생성:

`tox --recreate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py27</span>
