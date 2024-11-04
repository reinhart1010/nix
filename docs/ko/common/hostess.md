---
layout: page
title: common/hostess (한국어)
description: "`/etc/hosts` 파일 관리."
content_hash: c013ed11265e589279120bdfc20808428ff68376
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/hostess.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hostess

`/etc/hosts` 파일 관리.
더 많은 정보: <https://github.com/cbednarski/hostess>.

- 도메인, 대상 IP 주소 및 켜기/끄기 상태를 나열:

`hostess list`

- 호스트 파일에 컴퓨터를 가리키는 도메인을 추가:

`hostess add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>

- 호스트 파일에서 도메인을 제거:

`hostess del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local.example.com</span>

- 도메인 비활성화(제거하지는 않음):

`hostess off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local.example.com</span>
