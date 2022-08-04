---
layout: page
title: common/zipalign (English)
description: "Zip archive alignment tool."
content_hash: 6197a0be3d299e52d07efbdee1b59135a1305aee
---
# zipalign

Zip archive alignment tool.
Part of the Android SDK build tools.
More information: <https://developer.android.com/studio/command-line/zipalign>.

- Align the data of a ZIP file on 4-byte boundaries:

`zipalign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.zip</span>

- Check that a ZIP file is correctly aligned on 4-byte boundaries and display the results in a verbose manner:

`zipalign -v -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.zip</span>
