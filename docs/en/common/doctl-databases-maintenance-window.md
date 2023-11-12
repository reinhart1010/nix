---
layout: page
title: common/doctl-databases-maintenance-window (English)
description: "Schedule, and check the schedule of, maintenance windows for your databases."
content_hash: 619fba2a73b56e9a5580fe70fa0b4a7df8759d17
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl databases maintenance-window

Schedule, and check the schedule of, maintenance windows for your databases.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window>.

- Run a `doctl databases maintenance-window` command with an access token:

`doctl databases maintenance-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Retrieve details about a database cluster's maintenance windows:

`doctl databases maintenance-window get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>

- Update the maintenance window for a database cluster:

`doctl databases maintenance-window update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` --day `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">day_of_the_week</span>` --hour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hour_in_24_hours_format</span>
