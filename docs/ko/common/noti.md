---
layout: page
title: common/noti (한국어)
description: "프로세스를 모니터링하고 배너 알림을 트리거."
content_hash: 5b6492987aa170eceebdfc980cd6bab92120d9aa
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/noti.html
    icon: bi bi-globe
tldri18n_status: 2
---
# noti

프로세스를 모니터링하고 배너 알림을 트리거.
더 많은 정보: <https://github.com/variadico/noti>.

- tar가 파일 압축을 완료하면 알림 표시:

`noti `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cjf example.tar.bz2 example/</span>

- 감시할 명령어 뒤에 추가해도 알림 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">감시할_명령어</span>`; noti`

- PID를 통해 프로세스를 모니터링하고 PID가 사라지면 알림 트리거:

`noti -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>
