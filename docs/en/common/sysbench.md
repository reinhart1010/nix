---
layout: page
title: common/sysbench (English)
description: "Benchmark a System's CPU, IO and memory."
content_hash: 0f9e0ca2b1b3c056bc11390920f58b4c823e6802
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sysbench

Benchmark a System's CPU, IO and memory.
More information: <https://github.com/akopytov/sysbench/>.

- Run a CPU benchmark with 1 thread for 10 seconds:

`sysbench cpu run`

- Run a CPU benchmark with multiple threads for a specified time:

`sysbench --threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_threads</span>` --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- Run a memory benchmark with 1 thread for 10 seconds:

`sysbench memory run`

- Prepare a filesystem-level read benchmark:

`sysbench fileio prepare`

- Run a filesystem-level benchmark:

`sysbench --file-test-mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rndrd|rndrw|rndwr|seqrd|seqrewr|seqwr</span>` fileio run`
