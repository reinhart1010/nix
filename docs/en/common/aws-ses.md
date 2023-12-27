---
layout: page
title: common/aws-ses (English)
description: "CLI for AWS Simple Email Service."
content_hash: 0eed964526a72f7a42bbb45e07ff1c438ae64edc
last_modified_at: 2023-12-27
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ses.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ses

CLI for AWS Simple Email Service.
High-scale inbound and outbound cloud email service.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- Create a new receipt rule set:

`aws ses create-receipt-rule-set --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_set_name</span>` --generate-cli-skeleton`

- Describe the active receipt rule set:

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- Describe a specific receipt rule:

`aws ses describe-receipt-rule --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_set_name</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>` --generate-cli-skeleton`

- List all receipt rule sets:

`aws ses list-receipt-rule-sets --starting-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_string</span>` --max-items `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integer</span>` --generate-cli-skeleton`

- Delete a specific receipt rule set (the currently active rule set cannot be deleted):

`aws ses delete-receipt-rule-set --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_set_name</span>` --generate-cli-skeleton`

- Delete a specific receipt rule:

`aws ses delete-receipt-rule --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_set_name</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>` --generate-cli-skeleton`

- Send an email:

`aws ses send-email --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_address</span>` --destination "ToAddresses=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresses</span>`" --message "Subject={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject_text</span>`,Charset=utf8},Body={Text={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body_text</span>`,Charset=utf8},Html={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message_body_containing_html</span>`,Charset=utf8</span>`"`

- Display help for a specific SES subcommand:

`aws ses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`
