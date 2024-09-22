---
layout: page
title: common/aws-sqs (한국어)
description: "AWS SQS 서비스 대기열에 메시지 생성, 삭제 및 전송."
content_hash: dea5b27443e84c9c32aa8a1f3507df719b1059d7
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-sqs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-sqs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sqs

AWS SQS 서비스 대기열에 메시지 생성, 삭제 및 전송.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- 사용 가능한 모든 대기열 나열:

`aws sqs list-queues`

- 특정 대기열의 URL 표시:

`aws sqs get-queue-url --queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>

- JSON 형식의 파일에서 특정 속성을 사용하여 대기열을 생성:

`aws sqs create-queue --queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>` --attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://경로/대상/속성_파일.json</span>

- 특정 메시지를 대기열로 보냄:

`aws sqs send-message --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>` --message-body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지_본문</span>`" --delay-seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지연</span>` --message-attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://경로/대상/속성_파일.json</span>

- 대기열에서 지정된 메시지를 삭제:

`aws sqs delete-message --queue-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://queue_url</span>` --receipt-handle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receipt_handle</span>

- 특정 큐 삭제:

`aws sqs delete-queue --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>

- 지정된 대기열에서 모든 메시지를 삭제:

`aws sqs purge-queue --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>

- 대기열에 메시지를 보내려면, 특정 AWS 계정을 활성화:

`aws sqs add-permission --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">권한_이름</span>` --aws-account-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_아이디</span>` --actions SendMessage`
