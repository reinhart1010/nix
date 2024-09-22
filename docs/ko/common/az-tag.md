---
layout: page
title: common/az-tag (한국어)
description: "리소스에 대한 태그를 관리."
content_hash: 28a1ff8dd04363a0351913ad5fa6656b937928df
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/az-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az tag

리소스에 대한 태그를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/tag>.

- 태그 값 생성:

`az tag add-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_값</span>

- 구독에서 태그를 생성:

`az tag create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 구독에서 태그를 삭제:

`az tag delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 구독의 모든 태그 나열:

`az tag list --resource-id /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구독_아이디</span>

- 특정 태그 이름에 대한 태그 값 삭제:

`az tag remove-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_값</span>
