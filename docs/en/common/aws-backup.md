---
layout: page
title: common/aws-backup (English)
description: "Unified backup service designed to protect Amazon Web Services services and their associated data."
content_hash: 50deb294a0da8d99478575ef0c37d1979d4ce630
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/common/aws-backup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-backup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws backup

Unified backup service designed to protect Amazon Web Services services and their associated data.
More information: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Return BackupPlan details for a specific BackupPlanId:

`aws backup get-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Create a backup plan using a specific backup plan name and backup rules:

`aws backup create-backup-plan --backup-plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plan</span>

- Delete a specific backup plan:

`aws backup delete-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- List all active backup plans for the current account:

`aws backup list-backup-plans`

- Display details about your report jobs:

`aws backup list-report-jobs`
