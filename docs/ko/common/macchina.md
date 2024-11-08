---
layout: page
title: common/macchina (한국어)
description: "컴퓨터에 대한 정보를 표시."
content_hash: d87f67b03a2c84b20f9b5f315f7b2eb7512f4af1
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/macchina.html
    icon: bi bi-globe
tldri18n_status: 2
---
# macchina

컴퓨터에 대한 정보를 표시.
더 많은 정보: <https://github.com/Macchina-CLI/macchina>.

- 기본 설정 또는 구성 파일에 지정된 설정으로 시스템 정보 나열:

`macchina`

- 사용자 정의 구성 파일 경로 지정:

`macchina --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>

- 시스템 정보를 나열하되, 업타임, 셸 및 커널 출력을 길게 표시:

`macchina --long-uptime --long-shell --long-kernel`

- 시스템 정보를 가져올 때 발생한 오류/시스템 실패 점검:

`macchina --doctor`

- 모든 ASCII 아트의 원작자 나열:

`macchina --ascii-artists`
