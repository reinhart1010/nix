---
layout: page
title: common/apkleaks (English)
description: "An APK file scanner for exposing URIs, endpoints, and secrets."
content_hash: 77ba849f8db56d57c3e1c3f3e04150fe248cb107
last_modified_at: 2024-05-18
tldri18n_status: 2
---
# apkleaks

An APK file scanner for exposing URIs, endpoints, and secrets.
Note: APKLeaks utilizes the `jadx` disassembler to decompile APK files.
More information: <https://github.com/dwisiswant0/apkleaks>.

- Scan an APK [f]ile for URIs, endpoints, and secrets:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Scan and save the [o]utput to a specific file:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>

- Pass `jadx` disassembler [a]rguments:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>` --args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--threads-count 5 --deobf</span>`"`
