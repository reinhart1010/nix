---
layout: page
title: common/aws-sns (한국어)
description: "주제 및 구독을 만들고, 메시지를 보내고 받고, Amazon Simple Notification Service에 대한 이벤트 및 로그를 모니터링."
content_hash: e2a66e6babfd930e0fef0bc5d8738a2411a7eb89
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-sns.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sns

주제 및 구독을 만들고, 메시지를 보내고 받고, Amazon Simple Notification Service에 대한 이벤트 및 로그를 모니터링.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html>.

- 특정 유형의 모든 객체를 나열:

`aws sns list-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics</span>

- 특정 이름의 주제를 만들고 Amazon Resource Name (ARN)을 표시:

`aws sns create-topic --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 특정 ARN을 사용하여 주제에 대한 이메일 주소를 구독하고 구독 정보를 표시:

`aws sns subscribe --topic-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_ARN</span>` --protocol email --notification-endpoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>

- 특정 주제 또는 전화번호에 대한 메시지를 게시하고, 메시지 ID를 표시:

`aws sns publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100</span>` --message file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 해당 주제에서 특정 ARN이 있는 구독을 삭제:

`aws sns unsubscribe --subscription-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_ARN</span>

- 플랫폼 엔드포인트를 생성:

`aws sns create-platform-endpoint --platform-application-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform_application_ARN</span>` --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- 주제의 액세스 제어 정책에 설명 추가:

`aws sns add-permission --topic-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_ARN</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_label</span>` --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_id</span>` --action-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...</span>

- 특정 ARN을 사용하여 주제에 태그를 추가:

`aws sns tag-resource --resource-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_ARN</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Key=tag1_key Key=tag2_key,Value=tag2_value ...</span>
