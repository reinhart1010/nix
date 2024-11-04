---
layout: page
title: common/vf (한국어)
description: "VirtualFish는 Python 가상 환경을 관리하기 위한 fish shell 도구입니다."
content_hash: c09a88becb6e9e8d356864c2c606efc118219900
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vf

VirtualFish는 Python 가상 환경을 관리하기 위한 fish shell 도구입니다.
더 많은 정보: <https://virtualfish.readthedocs.io/en/latest/>.

- 가상 환경 생성:

`vf new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 특정 Python 버전으로 가상 환경 생성:

`vf new --python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local/bin/python3.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 지정한 가상 환경 활성화 및 사용:

`vf activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 현재 가상 환경을 현재 디렉토리에 연결하여 들어가면 자동으로 활성화하고 나가면 자동으로 비활성화:

`vf connect`

- 현재 가상 환경 비활성화:

`vf deactivate`

- 모든 가상 환경 나열:

`vf ls`

- 가상 환경 제거:

`vf rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상환경_이름</span>

- 도움말 표시:

`vf help`
