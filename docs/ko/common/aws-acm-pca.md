---
layout: page
title: common/aws-acm-pca (한국어)
description: "AWS 인증서 관리자 개인 인증 기관."
content_hash: edfc724ff716527f844065b8aad7c36ba27ac86d
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/aws-acm-pca.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-acm-pca.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws acm-pca

AWS 인증서 관리자 개인 인증 기관.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html>.

- 개인 인증 기관 생성:

`aws acm-pca create-certificate-authority --certificate-authority-configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_config</span>` --idempotency-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --permanent-deletion-time-in-days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- 개인 인증 기관 정보 표시:

`aws acm-pca describe-certificate-authority --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>

- 개인 인증 기관 목록:

`aws acm-pca list-certificate-authorities`

- 인증 기관 업데이트:

`aws acm-pca update-certificate-authority --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-authority-configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_config</span>` --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- 개인 인증 기관 삭제:

`aws acm-pca delete-certificate-authority --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>

- 인증서 발행:

`aws acm-pca issue-certificate --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-signing-request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert_signing_request</span>` --signing-algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` --validity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">validity</span>

- 인증서 취소:

`aws acm-pca revoke-certificate --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial</span>` --reason `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>

- 인증서 세부사항 출력:

`aws acm-pca get-certificate --certificate-authority-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_arn</span>` --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert_arn</span>
