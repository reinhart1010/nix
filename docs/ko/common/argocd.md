---
layout: page
title: common/argocd (한국어)
description: "Argo CD 서버를 제어하는 명령줄 인터페이스."
content_hash: 2928a845b9f2d16e5cfc3c1ae98b34aab8fb9b31
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/argocd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># argocd

Argo CD 서버를 제어하는 명령줄 인터페이스.
`argocd app`과 같은 일부 하위 명령에는 자체 사용 문서가 있습니다.
더 많은 정보: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Argo CD 서버에 로그인:

`argocd login --insecure --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argocd_서버:포트</span>

- 애플리케이션 목록 보여주기:

`argocd app list`
