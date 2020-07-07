# Automating AWS with Python

Repo for python code used to automated management of AWS resources

## 01-webotron

Webotron is a script to sync a local directory with an S3 bucket, and optionally configure Route53 and CloudFront

## Features

Webotron currently has the following features:

- List bucket
- List the contents of a bucket
- Create and setup a bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>
- Create a Route 53 record set

## 02-notifon

Notifon is a project to notify Slack users of changes to our AWS account using CloudWatch events.

## features
Notifon currently has the following features:

- Send notification to slack when an autoscaling event happens.

