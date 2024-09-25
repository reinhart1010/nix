---
layout: page
title: common/aws-pricing (한국어)
description: "Amazon Web Services에서 서비스, 제품 및 가격 정보를 쿼리."
content_hash: 316636fcd98df280e408634069088310d081cd07
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/aws-pricing.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-pricing.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws pricing

Amazon Web Services에서 서비스, 제품 및 가격 정보를 쿼리.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- 특정 지역의 서비스 코드 나열:

`aws pricing describe-services --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- 특정 지역의 지정된 서비스 코드에 대한 속성을 나열:

`aws pricing describe-services --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- 특정 지역의 서비스 코드에 대한 가격 정보 출력:

`aws pricing get-products --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- 특정 지역의 서비스 코드에 대한 특정 속성 값 나열:

`aws pricing get-attribute-values --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --attribute-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스타입</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- 인스턴스 유형 및 위치에 대한 필터를 사용하여, 서비스 코드에 대한 가격 정보를 출력:

`aws pricing get-products --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --filters "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)</span>`" --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>
