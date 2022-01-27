---
layout: page
title: linux/xinput (English)
description: "List available input devices, query information about a device and change input device settings."
content_hash: 3e7c814e8587bcec4e2ec260f723ee65b005f2f8
---
# xinput

List available input devices, query information about a device and change input device settings.
More information: <https://manned.org/xinput>.

- List all input devices:

`xinput list`

- Disable an input:

`xinput disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Enable an input:

`xinput enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Disconnect an input from its master:

`xinput float `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Reattach an input as slave to a master:

`xinput reattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master_id</span>

- List settings of an input device:

`xinput list-props `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Change a setting of an input device:

`xinput set-prop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setting_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
