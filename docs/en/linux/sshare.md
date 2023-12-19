---
layout: page
title: linux/sshare (English)
description: "List the shares of associations to a cluster."
content_hash: d85dcfea0091365c50609eb14f649301de586969
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# sshare

List the shares of associations to a cluster.
More information: <https://slurm.schedmd.com/sshare.html>.

- List Slurm share information:

`sshare`

- Control the output format:

`sshare --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parsable|parsable2|json|yaml</span>

- Control the fields to display:

`sshare --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format_string</span>

- Display information for the specified users only:

`sshare --users=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id_1,user_id_2,...</span>
