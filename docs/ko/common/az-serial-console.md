---
layout: page
title: common/az-serial-console (한국어)
description: "가상 머신의 직렬 콘솔에 연결."
content_hash: 74a3e6d076141872aeb7ff07414edff110d428db
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/az-serial-console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az serial-console

가상 머신의 직렬 콘솔에 연결.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/serial-console>.

- 직렬 콘솔에 연결:

`az serial-console connect --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹_이름</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_이름</span>

- 연결을 종료:

`<Ctrl>-]`
