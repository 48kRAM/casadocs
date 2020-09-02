

# User Account Setup 

Creating and setting up a user account on AWS

# Overview

To facilitate fine grain control of AWS resources, Amazon supplies two distinct account types. A Root user account (Account Root User) and Identity and Access Management Users (IAM Users). [Learn more.](http://docs.aws.amazon.com/general/latest/gr/root-vs-iam.html)

These accounts are distinct from regular Linux accounts that may exist on a compute instance.

# Account Root User

[Click here and follow the steps to set up an Amazon Web Services account.](http://www.dummies.com/programming/cloud-computing/amazon-web-services/set-up-your-amazon-web-services-account/)

Signing up for an AWS account automatically creates a Root user account with total control over the account. The credit card used during sign-up will be billed for all usage by the Account Root User and the Account\'s IAM Users.

In general, the Root user account should only be used for changing account wide settings, e.g. creating or removing IAM users, changing AWS support plan or closing the account. An IAM User account should be used when requesting resources. Following this model allows for finer grain control over the type and scale of resources a specific user can request, and can limit the risk from unexpected expenses or accidental global changes to the account.

# IAM Users

## Getting Started with IAM Users

[View Amazon\'s AWS Documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)

The Root Account User can create IAM Users. These IAM Users may have more limited permissions or they may have Administrators permissions. It is recommended the Root Account User first create an IAM User in the Administrators group. That IAM User can then login and perform essentially all administrative operations, including adding more IAM Users.

IAM users can be given different levels of permissions for requesting AWS resources. Perimissions can be mapped to a User via membership in an IAM group or by having an IAM Role mapped to the User. More information on creating and utilizing IAM groups and IAM Roles can be found [here](http://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

## How to Sign into AWS as an IAM User

[View Amazon\'s AWS Documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/console.html#user-sign-in-page)

## Best practices for using IAM Users

[View Amazon\'s AWS Documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users.)

# Linux Users

[View Amazon\'s AWS Documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)

IAM Users typically have the ability to start Instances, a virtual machine running Linux on AWS hardware. While starting the instance, an ssh key is specified. That key can be used to ssh into the running instance.

## Adding Additional Linux Users

[View Amazon\'s AWS Documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html)
