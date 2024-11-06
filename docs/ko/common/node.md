---
layout: page
title: common/node (한국어)
description: "서버 측 JavaScript 플랫폼 (Node.js)."
content_hash: f55ec42ff188d76de5a8ae4935aac732a6bd8764
last_modified_at: 2024-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/node.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/node.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/node.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/node.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/node.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
tldri18n_status: 2
---
# node

서버 측 JavaScript 플랫폼 (Node.js).
더 많은 정보: <https://nodejs.org>.

- JavaScript 파일 실행:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- REPL(대화형 셸) 시작:

`node`

- 지정된 파일을 실행하고 가져온 파일이 변경될 때 프로세스를 재시작 (Node.js 버전 18.11+ 필요):

`node --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 인수로 JavaScript 코드 평가:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>`"`

- 결과 평가 및 출력, node의 종속성 버전을 출력하는 데 유용:

`node -p "process.versions"`

- 인스펙터 활성화, 소스 코드가 완전히 구문 분석될 때까지 디버거가 연결될 때까지 실행 일시 중지:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
