---
layout: page
title: common/apkleaks (English)
description: "Expose URIs, endpoints, and secrets from APK files."
content_hash: 17519e5584e156b416b32a05e8869b0770bdb97f
last_modified_at: 2024-06-12
tldri18n_status: 2
---
# apkleaks

Expose URIs, endpoints, and secrets from APK files.
Note: APKLeaks utilizes the `jadx` disassembler to decompile APK files.
More information: <https://github.com/dwisiswant0/apkleaks>.

- Scan an APK [f]ile for URIs, endpoints, and secrets:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Scan and save the [o]utput to a specific file:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>

- Pass `jadx` disassembler [a]rguments:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>` --args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--threads-count 5 --deobf</span>`"`
