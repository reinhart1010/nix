---
layout: page
title: common/pypy (한국어)
description: "빠르고 호환성 있는 Python 언어의 대체 구현체."
content_hash: 5aad6d0f6e9266396cf6f09ef9dd64b98a412487
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pypy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pypy

빠르고 호환성 있는 Python 언어의 대체 구현체.
더 많은 정보: <https://doc.pypy.org>.

- REPL(대화형 셸) 시작:

`pypy`

- 주어진 Python 파일에서 스크립트 실행:

`pypy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 대화형 셸의 일부로 스크립트 실행:

`pypy -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- Python 표현식 실행:

`pypy -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>`"`

- 라이브러리 모듈을 스크립트로 실행 (옵션 목록 종료):

`pypy -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>

- pip를 사용하여 패키지 설치:

`pypy -m pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- Python 스크립트를 대화형으로 디버깅:

`pypy -m pdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>
