---
layout: page
title: linux/systemd-run (English)
description: "Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units."
content_hash: 7207ef09da4e00dc7a3758ff8eb1f4af26a6edbe
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/systemd-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-run

Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- Start a transient service:

`sudo systemd-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Start a transient service under the service manager of the current user (no privileges):

`systemd-run --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Start a transient service with a custom unit name and description:

`sudo systemd-run --unit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --description=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Start a transient service that does not get cleaned up after it terminates with a custom environment variable:

`sudo systemd-run --remain-after-exit --set-env=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Start a transient timer that periodically runs its transient service (see `man systemd.time` for calendar event format):

`sudo systemd-run --on-calendar=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">calendar_event</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Share the terminal with the program (allowing interactive input/output) and make sure the execution details remain after the program exits:

`systemd-run --remain-after-exit --pty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Set properties (e.g. CPUQuota, MemoryMax) of the process and wait until it exits:

`systemd-run --property MemoryMax=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory_in_bytes</span>` --property CPUQuota=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percentage_of_CPU_time</span>`% --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Use the program in a shell pipeline:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | systemd-run --pipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command3</span>
