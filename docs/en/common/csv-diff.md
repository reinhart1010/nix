---
layout: page
title: common/csv-diff (English)
description: "View differences between two CSV, TSV or JSON files."
content_hash: f735f6a4390897a1e999d70d6d7be6d3d990999e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# csv-diff

View differences between two CSV, TSV or JSON files.
More information: <https://github.com/simonw/csv-diff>.

- Display a human-readable summary of differences between files using a specific column as a unique identifier:

`csv-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.csv</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_name</span>

- Display a human-readable summary of differences between files that includes unchanged values in rows with at least one change:

`csv-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.csv</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_name</span>` --show-unchanged`

- Display a summary of differences between files in JSON format using a specific column as a unique identifier:

`csv-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.csv</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_name</span>` --json`
