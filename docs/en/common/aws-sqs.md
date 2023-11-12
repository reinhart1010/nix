---
layout: page
title: common/aws-sqs (English)
description: "Create, delete, and send messages to queues for the AWS SQS service."
content_hash: 9b2cb420c66e11b2b6f12fa7d57e31d02cc922e3
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/aws-sqs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sqs

Create, delete, and send messages to queues for the AWS SQS service.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- List all availables queues:

`aws sqs list-queues`

- Display the URL of a specific queue:

`aws sqs get-queue-url --queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- Create a queue with specific attributes from a file in JSON format:

`aws sqs create-queue --queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://path/to/attributes_file.json</span>

- Send a specific message to a queue:

`aws sqs send-message --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --message-body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message_body</span>`" --delay-seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delay</span>` --message-attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://path/to/attributes_file.json</span>

- Delete the specified message from a queue:

`aws sqs delete-message --queue-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://queue_url</span>` --receipt-handle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receipt_handle</span>

- Delete a specific queue:

`aws sqs delete-queue --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- Delete all messages from the specified queue:

`aws sqs purge-queue --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- Enable a specific AWS account to send messages to queue:

`aws sqs add-permission --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permission_name</span>` --aws-account-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_id</span>` --actions SendMessage`
