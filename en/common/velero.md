---
layout: page
title: common/velero (English)
description: "Backup and migrate Kubernetes applications and their persistent volumes."
content_hash: c13676cb263c9f2317f7dd389e890dfe4b1de3e2
---
# velero

Backup and migrate Kubernetes applications and their persistent volumes.
More information: <https://github.com/heptio/velero>.

- Create a backup containing all resources:

`velero backup create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_name</span>

- List all backups:

`velero backup get`

- Delete a backup:

`velero backup delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_name</span>

- Create a weekly backup, each living for 90 days (2160 hours):

`velero schedule create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schedule_name</span>` --schedules="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@every 7d</span>`" --ttl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2160h0m0s</span>

- Create a restore from the latest successful backup triggered by specific schedule:

`velero restore create --from-schedule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schedule_name</span>
