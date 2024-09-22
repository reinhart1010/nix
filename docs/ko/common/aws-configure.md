---
layout: page
title: common/aws-configure (한국어)
description: "AWS CLI 환경 설정 관리."
content_hash: 7b1282468f576e71f706edf0a4cd7f896d7de22b
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-configure.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-configure.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws-configure.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-configure.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws configure

AWS CLI 환경 설정 관리.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- AWS CLI를 대화형으로 구성 (새로운 환경을 설정하거나 기본값을 업데이트):

`aws configure`

- 대화형으로 AWS CLI에 대한 명명된 프로필을 구성 (새 프로필을 생성하거나, 기존 프로필을 업데이트):

`aws configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일_이름</span>

- 특정 환경 변수의 값을 표시:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 특정 프로필의 환경 변수 값을 표시:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일_이름</span>

- 특정 환경 변수의 값을 설정:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 특정 프로필의 환경 변수 값 설정:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일_이름</span>

- 구성 파일의 항목을 나열:

`aws configure list`

- 특정 프로필에 대한 환경 설정 항목 나열:

`aws configure list --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일_이름</span>
