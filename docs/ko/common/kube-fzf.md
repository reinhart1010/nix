---
layout: page
title: common/kube-fzf (한국어)
description: "Kubernetes Pod의 명령줄 퍼지 검색을 위한 셸 명령."
content_hash: e1c7f8153ca0ddc34919b1b754d9c432afc43833
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/kube-fzf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kube-fzf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kube-fzf

Kubernetes Pod의 명령줄 퍼지 검색을 위한 셸 명령.
관련 명령은 `kubectl`을 참고하세요.
더 많은 정보: <https://github.com/thecasualcoder/kube-fzf>.

- Pod 세부 정보 가져오기 (현재 네임스페이스에서):

`findpod`

- Pod 세부 정보 가져오기 (모든 네임스페이스에서):

`findpod -a`

- Pod 설명:

`describepod`

- Pod 로그 실시간 보기:

`tailpod`

- Pod의 컨테이너에 접속:

`execpod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">셸_명령어</span>

- Pod 포트 포워딩:

`pfpod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>
