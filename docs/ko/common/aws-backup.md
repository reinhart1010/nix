---
layout: page
title: common/aws-backup (한국어)
description: "Amazon Web Services와 관련 데이터를 보호하기 위해 설계된 통합 백업 서비스."
content_hash: ac0e59d63900abe540644b294f17b0ab9e5ef0a4
last_modified_at: 2023-09-20
related_topics:
  - title: English version
    url: /en/common/aws-backup.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws backup

Amazon Web Services와 관련 데이터를 보호하기 위해 설계된 통합 백업 서비스.
더 많은 정보: https://docs.aws.amazon.com/cli/latest/reference/backup/index.html.

- 특정 BackupPlanId에 대한 백업 계획 세부 정보 반환:

`aws backup get-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 특정 백업 계획 이름과 백업 규칙을 사용해 백업 계획 생성:

`aws backup create-backup-plan --backup-plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plan</span>

- 특정 백업 계획 삭제:

`aws backup delete-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 현재 계정에 대한 모든 활성 백업 계획 목록 반환:

`aws backup list-backup-plans`

- 보고서 작업에 대한 세부 정보 표시:

`aws backup list-report-jobs`