---
layout: page
title: common/crontab (English)
description: "Schedule cron jobs to run on a time interval for the current user."
content_hash: e121da00b1c508047462d533988c4270b5bb3cf7
related_topics:
  - title: italiano version
    url: /it/common/crontab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crontab.html
    icon: bi bi-globe
---
# crontab

Schedule cron jobs to run on a time interval for the current user.
Job definition format: "(min) (hour) (day_of_month) (month) (day_of_week) command_to_execute".
More information: <https://manned.org/crontab>.

- Edit the crontab file for the current user:

`crontab -e`

- Edit the crontab file for a specific user:

`sudo crontab -e -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Replace the current crontab with the contents of the given file:

`crontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View a list of existing cron jobs for current user:

`crontab -l`

- Remove all cron jobs for the current user:

`crontab -r`

- Sample job which runs at 10:00 every day (* means any value):

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_to_execute</span>

- Sample job which runs every minute on the 3rd of April:

`* * 3 Apr * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_to_execute</span>

- Sample job which runs a certain script at 02:30 every Friday:

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/absolute/path/to/script.sh</span>
