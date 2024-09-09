---
layout: page
title: common/aws-acm (한국어)
description: "AWS 인증서 관리자."
content_hash: 8793e49f3ce3a6a80b7d3a708da3251530537ac2
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/aws-acm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-acm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-acm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws acm

AWS 인증서 관리자.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- 인증서 가져오기:

`aws acm import-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>` --certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증서</span>` --private-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개인_키</span>` --certificate-chain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증서_체인</span>

- 인증서 나열:

`aws acm list-certificates`

- 인증서 설명 확인:

`aws acm describe-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- 인증서 요청:

`aws acm request-certificate --domain-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --validation-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검증_방법</span>

- 인증서 삭제:

`aws acm delete-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- 인증서 검증 방법 나열:

`aws acm list-certificates --certificate-statuses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- 인증서 세부 정보 출력:

`aws acm get-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- 인증서 옵션 업데이트:

`aws acm update-certificate-options --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>` --options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>
