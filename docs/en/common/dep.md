---
layout: page
title: common/dep (English)
description: "Deploy PHP applications."
content_hash: 9cc724f30b0db3e208ddf3a66f0fd0875691a79a
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/dep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dep

Deploy PHP applications.
Note: The Go command `dep` with the same name is deprecated and archived.
More information: <https://deployer.org>.

- Interactively initialize deployer in the local path (use a framework template with `--template=template`):

`dep init`

- Deploy an application to a remote host:

`dep deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Rollback to the previous working release:

`dep rollback`

- Connect to a remote host via ssh:

`dep ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- List commands:

`dep list`

- Run any arbitrary command on the remote hosts:

`dep run "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Display help for a command:

`dep help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
