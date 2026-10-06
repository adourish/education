# Storage — question review

Reviewed 129 questions. Found 12 problems.

## Confirmed wrong

### gh-667
**Stated answer:** Create S3 gateway endpoints, with the note "Interface endpoints are for private-link services, not S3."
**Should be:** Create interface endpoints (AWS PrivateLink) for Amazon S3.
**Why:** A gateway endpoint is only reachable from inside the VPC that holds the route-table entry — it cannot be used from an on-premises network over Direct Connect or VPN. Amazon S3 has supported interface endpoints since 2021, and that is the only option that keeps traffic off the internet from both the Region and the on-premises site, which is exactly what this question asks for. The explanation's claim about interface endpoints is also false.

### gh-534
**Stated answer:** Transition to S3 Standard-IA after 30 days, move all objects to S3 Glacier Flexible Retrieval after 90 days, and expire objects after 90 days.
**Should be:** The option that transitions to an infrequent-access class at day 30 and expires objects at day 90, with no Glacier step. Since high availability is only required for the first 30 days and the remaining 60 days are backup only, S3 One Zone-IA is the cheapest qualifying class.
**Why:** Transitioning to Glacier on the same day the objects are deleted does nothing except add a per-object transition request charge, so this answer cannot be the MOST cost-effective one. A lifecycle rule also cannot usefully transition and expire on the same day.

## Out of date

### wl-8
**Stated answer:** Launch an unencrypted EC2 instance, snapshot the root volume, then copy the snapshot with encryption — because "when launching an EC2 instance, the EBS volume for root cannot be encrypted."
**Now:** That restriction was removed in February 2019. You can turn on "EBS encryption by default" for an account in a Region, or set `Encrypted: true` (with a KMS key) on the root device in the launch block-device mapping, and the root volume is encrypted at launch straight from an unencrypted AMI. The snapshot-and-copy dance is no longer necessary, so this answer is stale.

### gh-205
**Stated answer:** Private S3 bucket with a bucket policy allowing a CloudFront origin access identity (OAI).
**Now:** Origin Access Control (OAC) replaced OAI in August 2022 and is what AWS recommends for S3 origins; OAI is documented as legacy and does not support SSE-KMS, dynamic requests, or all Regions. The shape of the answer (private bucket, CloudFront-only access) is still right, but the mechanism named is the superseded one.

### gh-302
**Stated answer:** CloudFront for delivery plus Amazon Elastic Transcoder to convert the video files.
**Now:** Amazon Elastic Transcoder is retired — AWS stopped accepting new customers in 2024 and the service reached end of support on 13 November 2025. The current service for this job is AWS Elemental MediaConvert.

### gh-49
**Stated answer:** S3 Intelligent-Tiering, lifecycle to S3 Glacier Flexible Retrieval after 1 year, Athena for recent files, S3 Glacier Select for archived files.
**Now:** S3 Glacier Select (and S3 Select) is no longer available to new customers as of mid-2024; existing users were grandfathered. The storage-class part of the answer is still the best of the options, but the retrieval mechanism named has been withdrawn — current practice is to restore the object and then query it.

### gh-501
**Stated answer:** Amazon Kinesis Data Firehose to ingest, Amazon Kinesis Data Analytics to analyse in real time.
**Now:** Both services have been renamed. Kinesis Data Analytics became Amazon Managed Service for Apache Flink in August 2023, and Kinesis Data Firehose became Amazon Data Firehose in February 2024. The architecture is still correct; only the names are stale. The old Firehose name also appears in gh-40, gh-226, gh-373 and gh-547.

## Explanation problems

### gh-46
**Issue:** The explanation has nothing to do with the question or the answer — it is boilerplate text about requesting service quota increases through the Service Quotas console. There is no justification given for using S3 as a transfer point with Macie scanning and SNS alerting.

### gh-517
**Issue:** The explanation argues against the stated answer. It says Systems Manager S3 logging "is primarily for storing the output of commands... not specifically for Session Manager logs" and "may not capture all the detailed session logs", which would rule out the option the answer picks. It is also wrong: Session Manager has a built-in S3 logging preference that writes full session output to a chosen bucket, which is why that option is the most operationally efficient one.

### gh-651
**Issue:** The explanation ends with a stray block answering a completely different question — "Answer: C) Configure the General Purpose SSD (gp3) EBS volume storage type and provision 15,000 IOPS", with notes about gp2 and magnetic volumes. It appears to be copy-paste contamination from an EBS question and has no bearing on the S3 lifecycle answer above it.

### gh-44
**Issue:** The explanation says MFA Delete "requires you to enter a one-time password from a multi-factor authentication (MFA) device before you can delete an object". That is not how it works. In a versioned bucket a plain DELETE just writes a delete marker and needs no MFA; MFA is required only to permanently delete a specific object version or to change the bucket's versioning state. The same incorrect description is repeated in gh-256.

### gh-22
**Issue:** The explanation states that S3 Intelligent-Tiering "can store objects in two access tiers: the frequent access tier and the infrequent access tier". Since November 2021 the automatic tiers are Frequent Access, Infrequent Access and Archive Instant Access, with optional Archive Access and Deep Archive Access tiers on top. The answer is right; the tier description is out of date, and the same two-tier claim is repeated in gh-212, gh-415 and gh-469.

Checked 129 questions: 2 stated answers are outright wrong, 5 are stale (retired, renamed or superseded AWS behaviour), and 5 have explanations that are unrelated, self-contradictory or factually wrong — overall the answer choices hold up well (roughly 95% defensible) but the explanations are unreliable and clearly stitched together from mixed community sources.
