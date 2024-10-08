---
layout: page
title: linux/systemd-ac-power (한국어)
description: "컴퓨터가 외부 전원에 연결되어 있는지 보고."
content_hash: 7d246bafa4502edb3bdf200444350c0117a2250f
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-ac-power.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-ac-power

컴퓨터가 외부 전원에 연결되어 있는지 보고.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-ac-power.html>.

- 조용히 확인하고 AC 전원에 연결되어 있을 때 0 상태 코드를 반환하고, 그렇지 않을 경우 비영 상태 코드를 반환:

`systemd-ac-power`

- 추가적으로 `stdout`에 `yes` 또는 `no`를 출력:

`systemd-ac-power --verbose`
