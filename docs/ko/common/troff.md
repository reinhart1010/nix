---
layout: page
title: common/troff (한국어)
description: "groff (GNU Troff) 문서 형식 시스템을 위한 조판 프로세서."
content_hash: 894a6ee9c071c387dec8bb74711984b9b521efb9
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/troff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# troff

groff (GNU Troff) 문서 형식 시스템을 위한 조판 프로세서.
같이 보기: `groff`.
더 많은 정보: <https://manned.org/troff>.

- 출력 형식을 PostScript 프린터용으로 지정하고, 출력을 파일에 저장:

`troff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.roff</span>` | grops > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ps</span>

- [me] 매크로 패키지를 사용하여 출력 형식을 PostScript 프린터용으로 지정하고, 출력을 파일에 저장:

`troff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.roff</span>` | grops > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ps</span>

- 출력 형식을 [a]SCII 텍스트로 지정하고 [man] 매크로 패키지를 사용:

`troff -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ascii</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">man</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.roff</span>` | grotty`

- 출력 형식을 [pdf] 파일로 지정하고, 출력을 파일에 저장:

`troff -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.roff</span>` | gropdf > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>
