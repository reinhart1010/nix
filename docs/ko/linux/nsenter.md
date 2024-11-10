---
layout: page
title: linux/nsenter (한국어)
description: "실행 중인 프로세스의 네임스페이스에서 새로운 명령을 실행합니다."
content_hash: 5d5c45094894b96f226ffcaff9d8d75b0b1c6bd6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/nsenter.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/nsenter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nsenter

실행 중인 프로세스의 네임스페이스에서 새로운 명령을 실행합니다.
Docker 이미지나 chroot 감옥에 특히 유용합니다.
더 많은 정보: <https://manned.org/nsenter>.

- 특정 프로세스와 동일한 네임스페이스를 사용하여 명령 실행:

`nsenter --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>

- 특정 프로세스의 마운트|UTS|IPC|네트워크|PID|사용자|cgroup|시간 네임스페이스에서 명령 실행:

`nsenter --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mount|uts|ipc|net|pid|user|cgroup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>

- 특정 프로세스의 UTS, 시간, IPC 네임스페이스에서 명령 실행:

`nsenter --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --uts --time --ipc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>

- procfs를 참조하여 특정 프로세스의 네임스페이스에서 명령 실행:

`nsenter --pid=/proc/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>`/pid/net -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>
