---
layout: page
title: common/eqn (한국어)
description: "groff (GNU Troff) 문서 형식화 시스템용 방정식 전처리."
content_hash: c5eacb25836a120ea9e329058f2b599961b32e41
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/eqn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eqn

groff (GNU Troff) 문서 형식화 시스템용 방정식 전처리.
참고: `troff` 및 `groff`.
더 많은 정보: <https://manned.org/eqn>.

- 방정식으로 입력을 처리하고, groff를 사용하여 향후 조판을 위해 출력을 PostScript에 저장:

`eqn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.eqn</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.roff</span>

- 매크로([me] macro) 패키지를 사용하여 방정식이 포함된 입력 파일을 PDF로 조판:

`eqn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.eqn</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>
