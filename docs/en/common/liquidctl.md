---
layout: page
title: common/liquidctl (English)
description: "Control liquid coolers."
content_hash: e4183bf2164eb6f96b830f8ac898c4ff3631a2e7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# liquidctl

Control liquid coolers.
More information: <https://github.com/liquidctl/liquidctl>.

- List available devices:

`liquidctl list`

- Initialize all supported devices:

`sudo liquidctl initialize all`

- Print the status of available liquid coolers:

`liquidctl status`

- Match a string in product name to pick a device and set its fan speed to 0% at 20°C, 50% at 50°C and 100% at 70°C:

`liquidctl --match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` set fan speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20 0 50 50 70 100</span>
