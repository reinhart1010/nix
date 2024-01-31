---
layout: page
title: common/in-toto-record (English)
description: "Create a signed link metadata file to provide evidence for supply chain steps."
content_hash: 78f31a7bce89a806e283c9fa47b827a35e2c6e91
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# in-toto-record

Create a signed link metadata file to provide evidence for supply chain steps.
More information: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>.

- Start the record (creates a preliminary link file):

`in-toto-record start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/edit_file1 path/to/edit_file2 ...</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Stop the record (expects a preliminary link file):

`in-toto-record stop -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/edit_file1 path/to/edit_file2 ...</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
