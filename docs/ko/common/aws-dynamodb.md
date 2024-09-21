---
layout: page
title: common/aws-dynamodb (한국어)
description: "예측 가능한 성능과 원활한 확장성을 갖춘 빠른 NoSQL 데이터베이스인 AWS Dynamodb 데이터베이스를 조작."
content_hash: 141ae572748e53f9355f4710bd1f96fe771c0f64
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-dynamodb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-dynamodb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws dynamodb

예측 가능한 성능과 원활한 확장성을 갖춘 빠른 NoSQL 데이터베이스인 AWS Dynamodb 데이터베이스를 조작.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

- 테이블 생성:

`aws dynamodb create-table --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` --attribute-definitions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AttributeName=S,AttributeType=S</span>` --key-schema `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AttributeName=S,KeyType=HASH</span>` --provisioned-throughput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ReadCapacityUnits=5,WriteCapacityUnits=5</span>

- DynamoDB의 모든 테이블 나열:

`aws dynamodb list-tables`

- 특정 테이블에 대한 세부정보 출력:

`aws dynamodb describe-table --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>

- 테이블에 항목 ㅊ두가:

`aws dynamodb put-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` --item '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"AttributeName": {"S": "value"}</span>`}'`

- 테이블에서 항목 검색:

`aws dynamodb get-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` --key '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ID": {"N": "1"}</span>`}'`

- 테이블의 항목 업데이트:

`aws dynamodb update-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` --key '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ID": {"N": "1"}</span>`}' --update-expression "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SET Name = :n</span>`" --expression-attribute-values '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{":n": {"S": "Jane"}</span>`}'`

- 테이블의 항목을 스캔:

`aws dynamodb scan --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>

- 테이블에서 항목 제거:

`aws dynamodb delete-item --table-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` --key '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ID": {"N": "1"}</span>`}'`
