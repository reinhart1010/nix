---
layout: page
title: common/az-lock (한국어)
description: "Azure 잠금 관리."
content_hash: 8cbc6539d03e58db9e6179e55495cace6289941e
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/az-lock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-lock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az lock

Azure 잠금 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/lock>.

- 읽기 전용 구독 수준의 잠금을 생성:

`az lock create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">잠금_이름</span>` --lock-type ReadOnly`

- 읽기 전용 리소스 그룹 수준 잠금을 생성:

`az lock create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">잠금_이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` --lock-type ReadOnly`

- 구독 수준 잠금을 해제:

`az lock delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">잠금_이름</span>

- 리소스 그룹 수준의 잠금을 삭제:

`az lock delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">잠금_이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 구독 수준의 모든 잠금을 나열:

`az lock list`

- 특정 이름([n])으로 구독 수준 잠금 표시:

`az lock show -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">잠금_이름</span>
