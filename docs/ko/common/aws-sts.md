---
layout: page
title: common/aws-sts (한국어)
description: "STS(Security Token Service)를 사용하면 IAM 사용자 또는 연합 사용자에 대한 임시 자격 증명을 요청."
content_hash: c78feaed84eaeb367d2e683950dca4e598c3cc96
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-sts.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-sts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sts

STS(Security Token Service)를 사용하면 IAM 사용자 또는 연합 사용자에 대한 임시 자격 증명을 요청.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- 특정 AWS 리소스에 액세스하려면, 임시 보안 자격 증명을 받아야 함:

`aws sts assume-role --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_role_arn</span>

- 작업을 호출하는 데 사용되는 자격 증명이 있는 IAM 사용자 또는 역할을 가져옴:

`aws sts get-caller-identity`
