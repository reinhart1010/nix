---
layout: page
title: common/watch (한국어)
description: "프로그램을 주기적으로 실행하여 전체 화면에 출력."
content_hash: e1e5ff8b0854b60afd26b9bfcf8397af18c5a27a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# watch

프로그램을 주기적으로 실행하여 전체 화면에 출력.
더 많은 정보: <https://manned.org/watch>.

- 명령을 반복 실행하고 결과를 표시:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 60초마다 명령을 재실행:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 디렉토리의 내용을 모니터링하고 변경된 부분을 강조:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- 파이프라인을 반복 실행하고 결과를 표시:

`watch '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_1</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_3</span>`'`
