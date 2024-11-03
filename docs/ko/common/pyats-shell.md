---
layout: page
title: common/pyats-shell (한국어)
description: "프로토타입 제작 시간을 절약하기 위해 미리 로드된 pyATS 대화형 Python 셸을 시작합니다."
content_hash: b3ac8f1ee604b82d37bb65cf0b2c8db31f3bb490
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pyats-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyats shell

프로토타입 제작 시간을 절약하기 위해 미리 로드된 pyATS 대화형 Python 셸을 시작합니다.
더 많은 정보: <https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_shell.html>.

- 정의된 테스트베드 파일과 함께 pyATS 셸 열기:

`pyats shell --testbed-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테스트베드.yaml</span>

- 정의된 Pickle 파일과 함께 pyATS 셸 열기:

`pyats shell --pickle-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/피클.file</span>

- IPython 비활성화 상태로 pyATS 열기:

`pyats shell --no-ipython`
