---
layout: page
title: common/pulumi-destroy (한국어)
description: "스택 내의 모든 기존 리소스를 제거합니다."
content_hash: bafcda0e4f5bc66d7940f50ed43716fd9c1dd4be
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pulumi-destroy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi destroy

스택 내의 모든 기존 리소스를 제거합니다.
더 많은 정보: <https://www.pulumi.com/docs/cli/commands/pulumi_destroy/>.

- 현재 스택의 모든 리소스를 제거:

`pulumi destroy`

- 특정 스택의 모든 리소스를 제거:

`pulumi destroy --stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택</span>

- 미리 보기 후 자동 승인하고 리소스를 제거:

`pulumi destroy --yes`

- 보호된 리소스를 제거 대상에서 제외:

`pulumi destroy --exclude-protected`

- 스택의 모든 리소스가 삭제된 후 스택 및 구성 파일 제거:

`pulumi destroy --remove`

- 오류가 발생해도 리소스 삭제를 계속 진행:

`pulumi destroy --continue-on-error`
