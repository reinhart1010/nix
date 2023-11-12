---
layout: page
title: common/fio (English)
description: "Flexible I/O tester."
content_hash: 00d98026299b9f02dba00775483ebd16dc2f5b2a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fio

Flexible I/O tester.
Tool that will spawn a number of threads or processes doing a particular type of I/O action.
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
