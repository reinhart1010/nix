---
layout: page
title: common/xxh (English)
description: "Bring your shell with all of your customizations through SSH sessions."
content_hash: 1ec68f339a5762bddbbc4691aaf5e5d612377b69
---
# xxh

Bring your shell with all of your customizations through SSH sessions.
Note: xxh does not install anything into system directories on the target machine; removing `~/.xxh` will clear all traces of xxh on the target machine.
More information: <https://github.com/xxh/xxh>.

- Connect to a host and run the current shell:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Install the current shell into the target machine without prompting:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++install`

- Run the specified shell on the target machine:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xonsh|zsh|fish|bash|osquery</span>

- Use a specific xxh configuration directory on the target machine:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++host-xxh-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.xxh</span>

- Use the specified configuration file on the host machine:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++xxh-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.config/xxh/config.xxhc</span>

- Specify a password to use for the SSH connection:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++password "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`"`

- Install an xxh package on the target machine:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++install-xxh-packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Set an environment variable for the shell process on the target machine:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`" ++env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
