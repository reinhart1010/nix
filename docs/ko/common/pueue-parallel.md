---
layout: page
title: common/pueue-parallel (한국어)
description: "병렬로 실행할 수 있는 허용 작업 수 설정."
content_hash: 242d4e90108965764373e6740a59dc96cda2b43d
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-parallel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue parallel

병렬로 실행할 수 있는 허용 작업 수 설정.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹에서 병렬로 실행할 수 있는 최대 작업 수 설정:

`pueue parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_병렬_작업_수</span>

- 특정 그룹에서 병렬로 실행할 수 있는 최대 작업 수 설정:

`pueue parallel --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_병렬_작업_수</span>
