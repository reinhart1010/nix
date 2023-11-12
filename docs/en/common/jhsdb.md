---
layout: page
title: common/jhsdb (English)
description: "Attach to a Java process or launch a postmortem debugger to analyze the core dump from a crashed Java Virtual Machine."
content_hash: 01061522d7bcec4b2ed6a672864cbe67ddbf9bb6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# jhsdb

Attach to a Java process or launch a postmortem debugger to analyze the core dump from a crashed Java Virtual Machine.
More information: <https://manned.org/jhsdb>.

- Print stack and locks information of a Java process:

`jhsdb jstack --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Open a core dump in interactive debug mode:

`jhsdb clhsdb --core `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/core_dump</span>` --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/jdk/bin/java</span>

- Start a remote debug server:

`jhsdb debugd --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --serverid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_unique_id</span>

- Connect to a process in interactive debug mode:

`jhsdb clhsdb --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
