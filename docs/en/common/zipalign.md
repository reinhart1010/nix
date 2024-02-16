---
layout: page
title: common/zipalign (English)
description: "Zip archive alignment tool."
content_hash: 7ab8c9cc095ad9276e3c3f6dbe929e8c63ed6617
last_modified_at: 2024-02-16
tldri18n_status: 2
---
# zipalign

Zip archive alignment tool.
Part of the Android SDK build tools.
More information: <https://developer.android.com/tools/zipalign>.

- Align the data of a ZIP file on 4-byte boundaries:

`zipalign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.zip</span>

- Check that a ZIP file is correctly aligned on 4-byte boundaries and display the results in a verbose manner:

`zipalign -v -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.zip</span>
