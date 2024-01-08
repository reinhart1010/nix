---
layout: page
title: common/gcloud-compute (English)
description: "Create, run, and manage VMs on Google Cloud infrastructure."
content_hash: 47e5d1d312345545adf7c985b3e04b1029705715
last_modified_at: 2024-01-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-compute.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud compute

Create, run, and manage VMs on Google Cloud infrastructure.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/compute>.

- List Compute Engine zones:

`gcloud compute zones list`

- Create a VM instance:

`gcloud compute instances create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>

- Display a VM instance's details:

`gcloud compute instances describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>

- List all VM instances in a project:

`gcloud compute instances list`

- Create a snapshot of a persistent disk:

`gcloud compute disks snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk_name</span>` --snapshot-names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>

- Display a snapshot's details:

`gcloud compute snapshots describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>

- Delete a snapshot:

`gcloud compute snapshots delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>

- Connect to a VM instance using SSH:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>
