---
layout: page
title: common/polybar-msg (English)
description: "Control `polybar` using inter-process-messaging (IPC)."
content_hash: e668e651ab4b396a8e42f0ddb96521a2df0b6e47
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# polybar-msg

Control `polybar` using inter-process-messaging (IPC).
Note: IPC is disabled by default and can be enabled by setting `enable-ipc = true` in the Polybar config.
More information: <https://polybar.rtfd.io/en/stable/user/ipc.html>.

- Quit the bar:

`polybar-msg cmd quit`

- Restart the bar in-place:

`polybar-msg cmd restart`

- Hide the bar (does nothing if the bar is already hidden):

`polybar-msg cmd hide`

- Show the bar again (does nothing if the bar is not hidden):

`polybar-msg cmd show`

- Toggle between hidden/visible:

`polybar-msg cmd toggle`

- Execute a module action (the data string is optional):

`polybar-msg action "#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_name</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_string</span>`"`

- Only send messages to a specific Polybar instance (all instances by default):

`polybar-msg -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmd|action</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">payload</span>
