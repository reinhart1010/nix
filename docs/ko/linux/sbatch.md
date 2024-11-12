---
layout: page
title: linux/sbatch (한국어)
description: "SLURM 스케줄러에 배치 작업 제출."
content_hash: 12f2dbfda9105372489385a98285563a9fc537c7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sbatch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sbatch

SLURM 스케줄러에 배치 작업 제출.
더 많은 정보: <https://manned.org/sbatch>.

- 배치 작업 제출:

`sbatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업.sh</span>

- 사용자 지정 이름으로 배치 작업 제출:

`sbatch --job-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myjob</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업.sh</span>

- 30분의 시간 제한으로 배치 작업 제출:

`sbatch --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">00:30:00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업.sh</span>

- 여러 노드를 요청하여 작업 제출:

`sbatch --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업.sh</span>
