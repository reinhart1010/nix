---
layout: page
title: common/aws-sns (English)
description: "Create topics and subscriptions, send and receive messages, and monitor events and logs for the Amazon Simple Notification Service."
content_hash: f459143b1e581a585a212271b65fefbefee2c340
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# aws sns

Create topics and subscriptions, send and receive messages, and monitor events and logs for the Amazon Simple Notification Service.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html>.

- List all objects of a specific type:

`aws sns list-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics</span>

- Create a topic with a specific name and show its Amazon Resource Name (ARN):

`aws sns create-topic --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Subscribe an email address to the topic with a specific ARN and show the subscription ARN:

`aws sns subscribe --topic-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_ARN</span>` --protocol email --notification-endpoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- Publish a message to a specific topic or phone number and show the message ID:

`aws sns publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100</span>` --message file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Delete the subscription with a specific ARN from its topic:

`aws sns unsubscribe --subscription-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_ARN</span>

- Create a platform endpoint:

`aws sns create-platform-endpoint --platform-application-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform_application_ARN</span>` --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Add a statement to a topic's access control policy:

`aws sns add-permission --topic-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_ARN</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_label</span>` --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_id</span>` --action-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...</span>

- Add a tag to the topic with a specific ARN:

`aws sns tag-resource --resource-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic_ARN</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Key=tag1_key Key=tag2_key,Value=tag2_value ...</span>
