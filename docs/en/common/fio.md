---
layout: page
title: common/fio (English)
description: "Flexible I/O tester: do an I/O action spawning multiple threads or processes."
content_hash: 4edf4035d0707db47b404d6dfeedcf2ad7a0ce71
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# fio

Flexible I/O tester: do an I/O action spawning multiple threads or processes.
More information: <https://fio.readthedocs.io/en/latest/fio_doc.html>.

- Test random reads:

`fio --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>` --eta-newline=1 --readonly`

- Test sequential reads:

`fio --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>` --eta-newline=1 --readonly`

- Test random read/write:

`fio --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>` --eta-newline=1`

- Test with parameters from a job file:

`fio `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/job_file</span>

- Convert a specific job file to command-line options:

`fio --showcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/job_file</span>
