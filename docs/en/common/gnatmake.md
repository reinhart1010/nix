---
layout: page
title: common/gnatmake (English)
description: "A low-level build tool for Ada programs (part of the GNAT toolchain)."
content_hash: a2f4fa69bd381ecda2a289320b6f0feeb993f328
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gnatmake

A low-level build tool for Ada programs (part of the GNAT toolchain).
More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Building-with-gnatmake.html>.

- Compile an executable:

`gnatmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file1.adb source_file2.adb ...</span>

- Set a custom executable name:

`gnatmake -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.adb</span>

- [f]orce recompilation:

`gnatmake -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.adb</span>
