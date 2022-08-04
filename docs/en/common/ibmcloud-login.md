---
layout: page
title: common/ibmcloud-login (English)
description: "Log in to the IBM Cloud."
content_hash: d40033b6af61a2d94a3e013733906091424a5a92
---
# ibmcloud login

Log in to the IBM Cloud.
More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

- Log in by using an interactive prompt:

`ibmcloud login`

- Log in to a specific API endpoint (default is `cloud.ibm.com`):

`ibmcloud login -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_endpoint</span>

- Log in by providing username, password and the targeted region as parameters:

`ibmcloud login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-south</span>

- Log in with an API key, passing it as an argument:

`ibmcloud login --apikey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_key_string</span>

- Log in with an API key, passing it as a file:

`ibmcloud login --apikey @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/api_key_file</span>

- Log in with a federated ID (single sign-on):

`ibmcloud login --sso`
