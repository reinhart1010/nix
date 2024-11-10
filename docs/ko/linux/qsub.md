---
layout: page
title: linux/qsub (한국어)
description: "스크립트를 큐 관리 시스템 TORQUE에 제출합니다."
content_hash: 264057366d505095d2ee70a3e1940e53e18be9ad
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/qsub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qsub

스크립트를 큐 관리 시스템 TORQUE에 제출합니다.
더 많은 정보: <https://manned.org/qsub.1>.

- 기본 설정으로 스크립트를 제출 (TORQUE 설정에 따라 다름):

`qsub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.sh</span>

- 1시간 2분 3초의 벽시계 실행 시간 제한을 지정하여 스크립트를 제출:

`qsub -l walltime=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.sh</span>

- 2개의 노드에서 각 노드당 4개의 코어를 사용하여 스크립트를 제출:

`qsub -l nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:ppn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.sh</span>

- 특정 큐에 스크립트를 제출 (다양한 큐는 최대 및 최소 실행 시간 제한이 다를 수 있음):

`qsub -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.sh</span>
