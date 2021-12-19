---
layout: page
title: linux/qsub (English)
description: "Submits a script to the queue management system TORQUE."
content_hash: 4a8119c8d56d7fc3a051d0b6401966bf1902c0a3
---
# qsub

Submits a script to the queue management system TORQUE.

- Submit a script with default settings (depends on TORQUE settings):

`qsub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>

- Submit a script with a specified wallclock runtime limit of 1 hour, 2 minutes and 3 seconds:

`qsub -l walltime=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>

- Submit a script that is executed on 2 nodes using 4 cores per node:

`qsub -l nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:ppn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>

- Submit a script to a specific queue. Note that different queues can have different maximum and minimum runtime limits:

`qsub -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.sh</span>
