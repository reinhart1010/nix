---
layout: page
title: common/pio-remote (English)
description: "Helper command for PlatformIO Remote Development."
content_hash: 817c4796cd8d7ae7c47cf7716b1b50c24b166961
---
# pio remote

Helper command for PlatformIO Remote Development.
`pio remote [command]` takes the same arguments as its locally executing counterpart `pio [command]`.
More information: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- List all active Remote Agents:

`pio remote agent list`

- Start a new Remote Agent with a specific name and share it with friends:

`pio remote agent start --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name</span>` --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example1@example.com</span>` --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example2@example.com</span>

- List devices from specified Agents (omit `--agent` to specify all Agents):

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name1</span>` --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name2</span>` device list`

- Connect to the serial port of a remote device:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name</span>` device monitor`

- Run all targets on a specified Agent:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name</span>` run`

- Update installed core packages, development platforms and global libraries on a specific Agent:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name</span>` update`

- Run all tests in all environments on a specific Agent:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_name</span>` test`
