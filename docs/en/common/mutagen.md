---
layout: page
title: common/mutagen (English)
description: "Real-time file synchronization and network forwarding tool."
content_hash: 396ad5ad8b6903fd2ccda4c35224788ec8d868b6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mutagen

Real-time file synchronization and network forwarding tool.
More information: <https://mutagen.io>.

- Start a synchronization session between a local directory and a remote host:

`mutagen sync create --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/local/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/remote/directory/</span>

- Start a synchronization session between a local directory and a Docker container:

`mutagen sync create --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/local/directory/</span>` docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/remote/directory/</span>

- Stop a running session:

`mutagen sync terminate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>

- Start a project:

`mutagen project start`

- Stop a project:

`mutagen project terminate`

- List running sessions for the current project:

`mutagen project list`
