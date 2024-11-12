---
layout: page
title: linux/sattach (한국어)
description: "Slurm 작업 단계에 연결."
content_hash: 8d44653b73cdde8198ff4b0e4cdee1c988acc642
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sattach.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sattach

Slurm 작업 단계에 연결.
더 많은 정보: <https://slurm.schedmd.com/sattach.html>.

- Slurm 작업 단계의 IO 스트림(`stdout`, `stderr`, `stdin`)을 현재 터미널로 리디렉션:

`sattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단계_ID</span>

- 현재 콘솔의 입력을 지정된 작업의 `stdin`으로 사용:

`sattach --input-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_번호</span>

- 지정된 작업의 `stdin`/`stderr`만 리디렉션:

`sattach --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력|오류</span>`-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_번호</span>
