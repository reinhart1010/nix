---
layout: page
title: common/az-devops (한국어)
description: "Azure DevOps 조직을 관리."
content_hash: 8dccafb87304b4eda9801226c3e21d74c2077cab
last_modified_at: 2024-09-16
related_topics:
  - title: English version
    url: /en/common/az-devops.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-devops.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az devops

Azure DevOps 조직을 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/devops>.

- 특정 조직에 로그인하려면 개인 액세스 토큰(PAT)을 설정:

`az devops login --organization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_url</span>

- 브라우저에서 프로젝트를 열기:

`az devops project show --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --open`

- 특정 프로젝트에 참여하는 특정 팀의 구성원을 나열:

`az devops team list-member --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --team `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팀_이름</span>

- Azure DevOps CLI 현재 구성을 확인:

`az devops configure --list`

- 기본 프로젝트와 기본 조직을 설정하여 Azure DevOps CLI 동작을 구성:

`az devops configure --defaults project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` organization=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_url</span>
