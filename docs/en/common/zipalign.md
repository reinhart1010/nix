---
layout: page
title: common/zipalign (English)
description: "Zip archive alignment tool."
content_hash: fa4a0f7af968ffe8a704c94a79bd9f58c7dd4521
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# zipalign

Zip archive alignment tool.
Part of the Android SDK build tools.
More information: <https://developer.android.com/tools/zipalign>.

- Align the data of a Zip file on 4-byte boundaries:

`zipalign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.zip</span>

- Check that a Zip file is correctly aligned on 4-byte boundaries and display the results in a verbose manner:

`zipalign -v -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.zip</span>
