---
layout: page
title: common/gnatprep (English)
description: "Preprocessor for Ada source code files (part of the GNAT toolchain)."
content_hash: aed24eedc0fa2f234c2a939f533c7aca3dcea49b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gnatprep

Preprocessor for Ada source code files (part of the GNAT toolchain).
More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>.

- Use symbol definitions from a file:

`gnatprep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">definitions_file</span>

- Specify symbol values in the command-line:

`gnatprep -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_file</span>
