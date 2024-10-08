---
layout: page
title: linux/systemd-cat (한국어)
description: "파이프라인 또는 프로그램의 출력 스트림을 systemd 저널과 연결."
content_hash: 5b4ca5cbb772d6b2034e62d897617efabb1188f9
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-cat

파이프라인 또는 프로그램의 출력 스트림을 systemd 저널과 연결.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cat.html>.

- 지정한 명령의 출력을 저널에 기록 (모든 출력 스트림이 캡처됨):

`systemd-cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 파이프라인의 출력을 저널에 기록 (`stderr`는 터미널에 연결된 상태 유지):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | systemd-cat`
