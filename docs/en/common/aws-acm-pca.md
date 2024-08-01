---
layout: page
title: common/aws-acm-pca (English)
description: "AWS Certificate Manager Private Certificate Authority."
content_hash: 1ebbb9058393f64498119a01b6cf991095f46c26
last_modified_at: 2024-08-01
tldri18n_status: 2
---
# aws acm-pca

AWS Certificate Manager Private Certificate Authority.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html>.

- Create a private certificate authority:

`aws acm-pca create-certificate-authority --certificate-authority-configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_config</span>` --idempotency-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --permanent-deletion-time-in-days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Describe a private certificate authority:

`aws acm-pca describe-certificate-authority --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>

- List private certificate authorities:

`aws acm-pca list-certificate-authorities`

- Update a certificate authority:

`aws acm-pca update-certificate-authority --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-authority-configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_config</span>` --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- Delete a private certificate authority:

`aws acm-pca delete-certificate-authority --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>

- Issue a certificate:

`aws acm-pca issue-certificate --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-signing-request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert_signing_request</span>` --signing-algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` --validity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">validity</span>

- Revoke a certificate:

`aws acm-pca revoke-certificate --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial</span>` --reason `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>

- Get certificate details:

`aws acm-pca get-certificate --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert_arn</span>
