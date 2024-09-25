---
layout: page
title: common/aws-lightsail (한국어)
description: "Amazon Lightsail 리소스 관리."
content_hash: 86e86340b00eb5f5641e777165404740b807dbd7
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/aws-lightsail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws lightsail

Amazon Lightsail 리소스 관리.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

- 모든 가상 사설 서버 또는 인스턴스를 나열:

`aws lightsail get-instances`

- 모든 번들 나열 (인스턴스 플랜):

`aws lightsail list-bundles`

- 사용 가능한 모든 인스턴스 이미지 또는 청사진을 나열:

`aws lightsail list-blueprints`

- 인스턴스 생성:

`aws lightsail create-instances --instance-names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --availability-zone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>` --bundle-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nano_2_0</span>` --blueprint-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">청사진_아이디</span>

- 특정 인스턴스의 상태를 출력:

`aws lightsail get-instance-state --instance-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 특정 인스턴스 중지:

`aws lightsail stop-instance --instance-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 특정 인스턴스 삭제:

`aws lightsail delete-instance --instance-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
