---
layout: page
title: common/argocd-app (한국어)
description: "Argo CD로 애플리케이션을 관리하는 명령줄 인터페이스."
content_hash: 2f674e319513b956a1873bdcc92efe5c64edffba
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/argocd-app.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/argocd-app.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd app

Argo CD로 애플리케이션을 관리하는 명령줄 인터페이스.
더 많은 정보: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- 애플리케이션 목록 보여주기:

`argocd app list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>` `

- 애플리케이션 세부사항 가져오기:

`argocd app get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>

- 애플리케이션을 내부적으로 (Argo CD가 실행되고 있는 동일한 클러스터에) 배포:

`argocd app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_레포지토리_주소</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레포지토리</span>` --dest-server https://kubernetes.default.svc --dest-namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 애플리케이션 삭제:

`argocd app delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 애플리케이션 자동 동기화 활성화:

`argocd app set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` --sync-policy auto --auto-prune --self-heal`

- 클러스터에 영향을 주지 않고 애플리케이션 동기화 미리보기:

`argocd app sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` --dry-run --prune`

- 애플리케이션 배포 기록 표시:

`argocd app history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wide|id</span>

- 히스토리 ID를 기준으로 이전 배포 버전으로 애플리케이션 롤백 (예상치 못한 리소스 삭제):

`argocd app rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">히스토리_id</span>` --prune`
