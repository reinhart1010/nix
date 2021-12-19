---
layout: page
title: common/black (한국어)
description: "Python 자동 코드 formatter."
content_hash: 8ac0f7a38ac5b628f80a408b7f617c142b764af1
related_topics:
  - title: English version
    url: /en/common/black.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/black.html
    icon: bi bi-globe
---
# black

Python 자동 코드 formatter.
더 많은 정보: <https://github.com/psf/black>.

- 파일 또는 전체 디렉토리의 자동 포맷:

`black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리/의/경로</span>

- 전달된 코드를 문자열로 포맷:

`black -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리/의/경로</span>

- 표준 출력시 각 파일에 대해 diff 출력:

`black --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리/의/경로</span>

- 파일을 다시 쓰지 않고 상태 반환:

`black --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리/의/경로</span>

- 파일 또는 디렉토리가 stderr에 배타적 오류 메시지를 발생시키는 자동 포맷:

`black --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리/의/경로</span>

- 작은 따옴표를 큰 따옴표로 바꾸지 않고 파일 또는 디렉토리 자동 서식 지정(채택 도우미, 새 프로젝트에 사용하지 마세요):

`black --skip-string-normalization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리/의/경로</span>
