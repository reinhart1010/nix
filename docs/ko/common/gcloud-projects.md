---
layout: page
title: common/gcloud-projects (한국어)
description: "Google Cloud에서 프로젝트 액세스 정책 관리."
content_hash: 042d97f5ad6651cad2c675a990745aeb0f4d2f83
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-projects.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud projects

Google Cloud에서 프로젝트 액세스 정책 관리.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/projects>.

- 새 프로젝트 생성:

`gcloud projects create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_아이디|프로젝트_번호</span>

- 모든 활성 프로젝트 나열:

`gcloud projects list`

- 프로젝트의 메타데이터 표시:

`gcloud projects describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_아이디</span>

- 프로젝트 삭제:

`gcloud projects delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_아이디|프로젝트_번호</span>

- 지정된 프로젝트에 IAM 정책 바인딩 추가:

`gcloud projects add-iam-policy-binding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_아이디</span>` --member `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주체</span>` --role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>
