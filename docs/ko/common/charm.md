---
layout: page
title: common/charm (한국어)
description: "사용자 계정, 데이터 저장 및 암호화에 대해 걱정하지 않고 터미널 기반 애플리케이션에 백엔드를 추가할 수 있는 도구 세트."
content_hash: 4fa80359a711e52c09a5a3e82d8ae03a5e62265d
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/charm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# charm

사용자 계정, 데이터 저장 및 암호화에 대해 걱정하지 않고 터미널 기반 애플리케이션에 백엔드를 추가할 수 있는 도구 세트.
더 많은 정보: <https://github.com/charmbracelet/charm>.

- Charm 계정 키를 백업:

`charm backup-keys`

- Charm 계정 키를 특정 위치에 백업:

`charm backup-keys -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tar</span>

- 이전에 백업한 Charm 계정 키 가져오기:

`charm import-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">charm-키-백업.tar</span>`"`

- 컴퓨터에서 `cloud.charm.sh` 폴더가 있는 위치를 발견:

`charm where`

- Charm 서버를 시작:

`charm serve`

- 연결된 SSH 키 인쇄:

`charm keys`

- Charm ID를 인쇄:

`charm id`
