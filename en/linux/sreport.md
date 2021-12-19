---
layout: page
title: linux/sreport (English)
description: "Generate reports on jobs, users, and clusters from accounting data."
content_hash: 8d6a220557966205d38c87757b741dff61757541
---
# sreport

Generate reports on jobs, users, and clusters from accounting data.
More information: <https://slurm.schedmd.com/sreport.html>.

- Show pipe delimited cluster utilization data:

`sreport --parsable cluster utilization`

- Show number of jobs run:

`sreport job sizes printjobcount`

- Show users with the highest CPU time use:

`sreport user topuser`
