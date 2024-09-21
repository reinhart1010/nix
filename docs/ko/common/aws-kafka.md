---
layout: page
title: common/aws-kafka (한국어)
description: "Amazon MSK (Apache Kafka용 관리형 스트리밍) 클러스터 관리."
content_hash: aa2f1cb30a2f4d9fef165fb17855bbbf887b0f80
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-kafka.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-kafka.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws kafka

Amazon MSK (Apache Kafka용 관리형 스트리밍) 클러스터 관리.
추가 정보: `aws`.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

- 새로운 MSK 클러스터 만들기:

`aws kafka create-cluster --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --broker-node-group-info instanceType=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_타입</span>`,clientSubnets=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브넷_아이디1 서브넷_아이디2 ...</span>` --kafka-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` --number-of-broker-nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- MSK 클러스터 정보 표시:

`aws kafka describe-cluster --cluster-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_arn</span>

- 현재 지역의 모든 MSK 클러스터 목록 나열:

`aws kafka list-clusters`

- 새로운 MSK 구성 파일 생성:

`aws kafka create-configuration --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성파일_이름</span>` --server-properties file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성파일_이름.txt</span>

- MSK 구성파일 내용 표시:

`aws kafka describe-configuration --arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_arn</span>

- 현재 지역의 모든 MSK 구성 나열:

`aws kafka list-configurations`

- MSK 클러스터 구성 업데이트:

`aws kafka update-cluster-configuration --cluster-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_arn</span>` --configuration-info arn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_arn</span>`,revision=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_revision</span>

- MSK 클러스터 삭제:

`aws kafka delete-cluster --cluster-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_arn</span>
