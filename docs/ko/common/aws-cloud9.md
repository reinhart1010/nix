---
layout: page
title: common/aws-cloud9 (한국어)
description: "AWS Cloud9은 클라우드에서 소프트웨어를 작성, 빌드, 실행, 테스트, 디버그 및 릴리스하는 도구 모음입니다."
content_hash: 46ccec22e52b4c5387437b3c13c5ebcd4baf20a3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-cloud9.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cloud9

AWS Cloud9은 클라우드에서 소프트웨어를 작성, 빌드, 실행, 테스트, 디버그 및 릴리스하는 도구 모음입니다.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html>.

- Cloud9 개발 환경 식별자 목록 가져오기:

`aws cloud9 list-environments`

- Cloud9 개발 환경 만들기:

`aws cloud9 create-environment-ec2 --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --instance-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_type</span>

- Cloud9 개발 환경에 대한 정보 표시:

`aws cloud9 describe-environments --environment-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_ids</span>

- Cloud9 개발 환경에 환경 멤버 추가:

`aws cloud9 create-environment-membership --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>` --user-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_arn</span>` --permissions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permissions</span>

- Cloud9 개발 환경에 대한 상태 정보 표시:

`aws cloud9 describe-environment-status --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>

- Cloud9 환경 삭제:

`aws cloud9 delete-environment --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>

- 개발 환경에서 환경 멤버 삭제:

`aws cloud9 delete-environment-membership --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>` --user-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_arn</span>
