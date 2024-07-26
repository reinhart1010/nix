---
layout: page
title: linux/filefrag (English)
description: "Report how badly fragmented a particular file might be."
content_hash: dbf3f1976f11266bc866a8d8ba3853894890a841
last_modified_at: 2024-07-26
tldri18n_status: 2
---
# filefrag

Report how badly fragmented a particular file might be.
More information: <https://manned.org/filefrag>.

- Display a report for one or more files:

`filefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display a report using a 1024 byte blocksize:

`filefrag -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a report using a certain blocksize:

`filefrag -b`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024|1K|1M|1G|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sync the file before requesting the mapping:

`filefrag -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display mapping of extended attributes:

`filefrag -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display a report with verbose information:

`filefrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
