---
layout: page
title: common/aws-backup (English)
description: "Unified backup service designed to protect Amazon Web Services services and their associated data."
content_hash: 39e4227afb9ddc8a2abddf71b43f3a114c085978
last_modified_at: 2022-12-17
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws backup

Unified backup service designed to protect Amazon Web Services services and their associated data.
More information: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Return BackupPlan details for a specific BackupPlanId:

`aws backup get-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Create a backup plan using a specific backup plan name and backup rules:

`aws backup create-backup-plan --backup-plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plan</span>

- Delete a specific backup plan:

`aws backup delete-backup-plan --backup-plan-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Return a list of all active backup plans for the current account:

`aws backup list-backup-plans`

- Display details about your report jobs:

`aws backup list-report-jobs`
