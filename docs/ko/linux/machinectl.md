---
layout: page
title: linux/machinectl (한국어)
description: "systemd 머신 관리자를 제어합니다."
content_hash: ec4f3eef77891a82b16361881cd4d3a86cf3a5b2
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/machinectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# machinectl

systemd 머신 관리자를 제어합니다.
가상 머신, 컨테이너 및 이미지에서 작업을 실행합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- `systemd-nspawn`을 사용하여 서비스를 머신으로 시작:

`sudo machinectl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">머신_이름</span>

- 실행 중인 머신 중지:

`sudo machinectl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">머신_이름</span>

- 실행 중인 머신 목록 표시:

`machinectl list`

- 머신 내부에서 대화형 셸 열기:

`sudo machinectl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">머신_이름</span>
