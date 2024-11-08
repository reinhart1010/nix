---
layout: page
title: common/rscript (한국어)
description: "R 프로그래밍 언어로 스크립트를 실행."
content_hash: a39102cc8f26d9e8c00e82baa007d0a898affec3
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Rscript

R 프로그래밍 언어로 스크립트를 실행.
더 많은 정보: <https://www.r-project.org>.

- 스크립트 실행:

`Rscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.R</span>

- 바닐라 모드로 스크립트 실행 (세션을 빈 상태로 시작하며 종료 시 작업 공간을 저장하지 않음):

`Rscript --vanilla `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.R</span>

- 하나 이상의 R 표현식 실행:

`Rscript -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식1</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식2</span>

- R 버전 표시:

`Rscript --version`
