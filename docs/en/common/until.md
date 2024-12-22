---
layout: page
title: common/until (English)
description: "Simple shell loop that repeats until it receives zero as return value."
content_hash: 0a5a34e61a1d4e9e035d47b4b62d051c0f1c52e4
last_modified_at: 2024-12-22
tldri18n_status: 2
---
# until

Simple shell loop that repeats until it receives zero as return value.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-until>.

- Execute a command until it succeeds:

`until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; do :; done`

- Wait for a systemd service to be active:

`until systemctl is-active --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Waiting..."</span>`; sleep 1; done; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Launched!"</span>
