---
layout: page
title: linux/qsub (English)
description: "Submits a script to the queue management system TORQUE."
content_hash: 8cab03ed5f070968b9ea834fb193aeef072f4745
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qsub

Submits a script to the queue management system TORQUE.
More information: <https://manned.org/qsub.1>.

- Submit a script with default settings (depends on TORQUE settings):

`qsub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>

- Submit a script with a specified wallclock runtime limit of 1 hour, 2 minutes and 3 seconds:

`qsub -l walltime=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>

- Submit a script that is executed on 2 nodes using 4 cores per node:

`qsub -l nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:ppn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>

- Submit a script to a specific queue. Note that different queues can have different maximum and minimum runtime limits:

`qsub -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>
