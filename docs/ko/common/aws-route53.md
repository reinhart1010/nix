---
layout: page
title: common/aws-route53 (한국어)
description: "AWS Route53용 CLI - Route 53은 가용성과 확장성이 뛰어난 DNS(도메인 네임 시스템) 웹 서비스입니다."
content_hash: 3ada095e44119c4b9fdd0e6834a87ac5b3bee327
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/aws-route53.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-route53.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws route53

AWS Route53용 CLI - Route 53은 가용성과 확장성이 뛰어난 DNS(도메인 네임 시스템) 웹 서비스입니다.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- 모든 호스팅 영역(프라이빗 및 퍼블릭)을 나열:

`aws route53 list-hosted-zones`

- 존의 모든 레코드 표시:

`aws route53 list-resource-record-sets --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">존_아이디</span>

- 작업을 안전하게 재시도하려면, 요청 식별자를 사용해 새로운 공개 존을 생성:

`aws route53 create-hosted-zone --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --caller-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">요청_구분자</span>

- 존 삭제 (존에 기본 값이 아닌 SOA가 존재하며, NS 레코드가 있는 경우 명령어 실행이 실패):

`aws route53 delete-hosted-zone --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">존_아이디</span>

- 특정 영역의 Amazon 서버에서 DNS 확인을 테스트:

`aws route53 test-dns-answer --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">존_아이디</span>` --record-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --record-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>
