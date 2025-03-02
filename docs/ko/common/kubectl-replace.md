---
layout: page
title: common/kubectl-replace (한국어)
description: "파일 또는 `stdin`을 통해 리소스를 교체."
content_hash: 4ea357ef9b3d7f9899c6c947140bc58f73782cb2
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectl-replace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl replace

파일 또는 `stdin`을 통해 리소스를 교체.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- 리소스 정의 파일을 사용하여 리소스 교체:

`kubectl replace -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yml</span>

- `stdin`으로 전달된 입력을 사용하여 리소스 교체:

`kubectl replace -f -`

- 강제로 교체: 리소스를 삭제한 후 다시 생성:

`kubectl replace --force -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yml</span>
