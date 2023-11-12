---
layout: page
title: common/kiwi-ng (English)
description: "KIWI NG is an OS image and appliance builder."
content_hash: d790a65a23ce07cfd7b4c4a25aced5a52ffd6602
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kiwi-ng

KIWI NG is an OS image and appliance builder.
More information: <https://osinside.github.io/kiwi/>.

- Build an appliance:

`kiwi-ng system build --description=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --target-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show build result of built appliance:

`kiwi-ng result list --target-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display help:

`kiwi-ng help`

- Display version:

`kiwi-ng -v`
