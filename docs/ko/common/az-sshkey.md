---
layout: page
title: common/az-sshkey (한국어)
description: "가상 머신으로 SSH 공개 키를 관리."
content_hash: 8f01a38ad70fb4e6ce59c76f0cffd9e1c8a008b0
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/az-sshkey.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-sshkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az sshkey

가상 머신으로 SSH 공개 키를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/sshkey>.

- 새로운 SSH 키를 생성:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 기존 SSH 키 업로드:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --public-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@path/to/key.pub</span>`"`

- 모든 SSH 공개 키를 나열:

`az sshkey list`

- SSH 공개 키를 대한 정보 표시:

`az sshkey show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>
