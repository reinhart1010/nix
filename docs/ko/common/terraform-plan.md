---
layout: page
title: common/terraform-plan (한국어)
description: "Terraform 실행 계획을 생성하고 보여줍니다."
content_hash: ea3fdf64f81ee4331a45a81e242860873114d30d
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/terraform-plan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/terraform-plan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terraform plan

Terraform 실행 계획을 생성하고 보여줍니다.
더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/plan>.

- 현재 디렉토리에서 실행 계획 생성 및 보기:

`terraform plan`

- 현재 존재하는 모든 원격 객체를 삭제하는 계획 보기:

`terraform plan -destroy`

- Terraform 상태 및 출력 값을 업데이트하는 계획 보기:

`terraform plan -refresh-only`

- 입력 변수에 대한 값 지정:

`terraform plan -var '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값1</span>`' -var '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값2</span>`'`

- 특정 리소스 하위 집합에만 Terraform의 주의 집중:

`terraform plan -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type.resource_name[인스턴스 인덱스]</span>

- 계획을 JSON으로 출력:

`terraform plan -json`

- 특정 파일에 계획 기록:

`terraform plan -no-color > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
