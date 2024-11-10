---
layout: page
title: linux/taskset (한국어)
description: "프로세스의 CPU 친화도를 가져오거나 설정하거나 정의된 CPU 친화도로 새 프로세스를 시작합니다."
content_hash: a8dbdf48e177fca72f01834b371ccf17aa405bc1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/taskset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# taskset

프로세스의 CPU 친화도를 가져오거나 설정하거나 정의된 CPU 친화도로 새 프로세스를 시작합니다.
더 많은 정보: <https://manned.org/taskset>.

- 실행 중인 프로세스의 PID로 CPU 친화도 가져오기:

`taskset --pid --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 실행 중인 프로세스의 PID로 CPU 친화도 설정:

`taskset --pid --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 단일 CPU에 대한 친화도로 새 프로세스 시작:

`taskset --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 여러 비연속 CPU에 대한 친화도로 새 프로세스 시작:

`taskset --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_2</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_3</span>

- CPU 1부터 4까지의 친화도로 새 프로세스 시작:

`taskset --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_1</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_4</span>
