---
layout: page
title: common/aws-acm (English)
description: "AWS Certificate Manager."
content_hash: 955ec998df66db9370ef4c5b16c8aede697080c1
last_modified_at: 2024-07-31
tldri18n_status: 2
---
# aws acm

AWS Certificate Manager.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- Import a certificate:

`aws acm import-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>` --certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate</span>` --private-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">private_key</span>` --certificate-chain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_chain</span>

- List certificates:

`aws acm list-certificates`

- Describe a certificate:

`aws acm describe-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- Request a certificate:

`aws acm request-certificate --domain-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --validation-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">validation_method</span>

- Delete a certificate:

`aws acm delete-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- List certificate validations:

`aws acm list-certificates --certificate-statuses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- Get certificate details:

`aws acm get-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- Update certificate options:

`aws acm update-certificate-options --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>` --options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>
