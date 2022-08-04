---
layout: page
title: linux/filefrag (English)
description: "Report how badly fragmented a particular file might be."
content_hash: d56d7e6c4eff1e8787949899f855ff42ed25dc30
---
# filefrag

Report how badly fragmented a particular file might be.
More information: <https://manned.org/filefrag>.

- Display a report for a specific file:

`filefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a report for space-separated list of files:

`filefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Display a report using a 1024 byte blocksize:

`filefrag -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sync the file before requesting the mapping:

`filefrag -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>

- Display mapping of extended attributes:

`filefrag -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>

- Display a report with verbose information:

`filefrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>
