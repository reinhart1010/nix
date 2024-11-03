---
layout: page
title: common/pycodestyle (한국어)
description: "Python 코드를 PEP 8 스타일 규칙에 맞게 검사."
content_hash: 5da259b4c9fad43765ee95aa38df25ff89724306
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pycodestyle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pycodestyle

Python 코드를 PEP 8 스타일 규칙에 맞게 검사.
더 많은 정보: <https://pycodestyle.readthedocs.io>.

- 단일 파일의 스타일 검사:

`pycodestyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py</span>

- 여러 파일의 스타일 검사:

`pycodestyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.py 파일2.py ...</span>

- 오류의 첫 번째 발생만 표시:

`pycodestyle --first `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py</span>

- 각 오류에 대한 소스 코드 표시:

`pycodestyle --show-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py</span>

- 각 오류에 대한 특정 PEP 8 텍스트 표시:

`pycodestyle --show-pep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py</span>
