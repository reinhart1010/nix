---
layout: page
title: linux/systemd-detect-virt (한국어)
description: "가상화된 환경에서 실행 여부를 감지."
content_hash: 3e64165aeff74945bba49cf9b25a289ed3cac4fb
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-detect-virt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-detect-virt

가상화된 환경에서 실행 여부를 감지.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-detect-virt.html>.

- 감지 가능한 가상화 기술 목록 표시:

`systemd-detect-virt --list`

- 가상화 여부를 감지하고 결과를 출력하며, VM이나 컨테이너에서 실행 중이면 0 상태 코드를 반환하고, 그렇지 않으면 0이 아닌 코드를 반환:

`systemd-detect-virt`

- 아무것도 출력하지 않고 조용히 확인:

`systemd-detect-virt --quiet`

- 컨테이너 가상화만 감지:

`systemd-detect-virt --container`

- 하드웨어 가상화만 감지:

`systemd-detect-virt --vm`
