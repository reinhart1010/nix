---
layout: page
title: common/pic (한국어)
description: "groff (GNU Troff) 문서 형식 시스템을 위한 그림 전처리기."
content_hash: 12b0d883d1ddefce906e6997e9c892ee6551024a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pic

groff (GNU Troff) 문서 형식 시스템을 위한 그림 전처리기.
같이 보기: `groff`, `troff`.
더 많은 정보: <https://manned.org/pic>.

- 그림이 포함된 입력을 처리하고, 나중에 groff를 사용하여 PostScript로 조판하기 위해 출력 저장:

`pic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pic</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.roff</span>

- [me] 매크로 패키지를 사용하여 그림이 포함된 입력을 PDF로 조판:

`pic -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pic</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>
