---
layout: page
title: common/gcloud-iam (한국어)
description: "Identity and Access Management (IAM) 환경 설정 및 서비스 계정을 구성합니다."
content_hash: a758c17228059129bafef91d911180a52179f658
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-iam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud iam

Identity and Access Management (IAM) 환경 설정 및 서비스 계정을 구성합니다.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/iam>.

- 리소스에 대한 IAM 부여 가능한 역할 나열:

`gcloud iam list-grantable-roles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스</span>

- 조직 또는 프로젝트에 대한 사용자 정의 역할 생성:

`gcloud iam roles create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직|프로젝트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직|프로젝트_아이디</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/role.yaml</span>

- 프로젝트에 대한 서비스 계정 생성:

`gcloud iam service-accounts create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 서비스 계정에 IAM 정책 바인딩 추가:

`gcloud iam service-accounts add-iam-policy-binding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_계정_이메일</span>` --member `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">멤버</span>` --role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>

- 기존 IAM 정책 바인딩 교체:

`gcloud iam service-accounts set-iam-policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_계정_이메일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책_파일</span>

- 서비스 계정의 키 나열:

`gcloud iam service-accounts keys list --iam-account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_계정_이메일</span>
