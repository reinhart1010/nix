---
layout: page
title: common/yapf (한국어)
description: "Python 스타일 가이드 검사기."
content_hash: e37f68dbd771f1ed79f6a34da697c61124e07d0d
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/yapf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yapf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yapf

Python 스타일 가이드 검사기.
더 많은 정보: <https://github.com/google/yapf>.

- 변경 사항을 적용하지 않고 변경 사항의 차이를 표시 (드라이런):

`yapf --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 제자리에서 포맷하고 변경 사항의 차이를 표시:

`yapf --diff --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉토리 내의 모든 Python 파일을 재귀적으로 동시에 포맷:

`yapf --recursive --in-place --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep8</span>` --parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
