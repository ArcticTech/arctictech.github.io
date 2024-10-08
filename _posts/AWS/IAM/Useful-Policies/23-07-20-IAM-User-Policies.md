---
title: IAM User Policies
date: 2023-07-20 03:03:00 -700
categories: [Aws-iam,Useful-Policies]
tags: [aws,iam]
---

## IAM User Policies
* Limited Admin Policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Permissions",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*"
        },
        {
            "Sid": "EditSelf",
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceSpecificCredential",
                "iam:ListServiceSpecificCredentials",
                "iam:UpdateServiceSpecificCredential",
                "iam:DeleteServiceSpecificCredential",
                "iam:ResetServiceSpecificCredential",
                "iam:DeleteSSHPublicKey",
                "iam:GetSSHPublicKey",
                "iam:ListSSHPublicKeys",
                "iam:UpdateSSHPublicKey",
                "iam:UploadSSHPublicKey",
                "iam:CreateAccessKey",
                "iam:DeleteAccessKey",
                "iam:GetAccessKeyLastUsed",
                "iam:ListAccessKeys",
                "iam:UpdateAccessKey",
                "iam:CreateVirtualMFADevice",
                "iam:DeactivateMFADevice",
                "iam:DeleteVirtualMFADevice",
                "iam:EnableMFADevice",
                "iam:ListMFADevices",
                "iam:ResyncMFADevice",
                "iam:DeleteSigningCertificate",
                "iam:ListSigningCertificates",
                "iam:UpdateSigningCertificate",
                "iam:UploadSigningCertificate",
                "iam:ChangePassword"
            ],
            "Resource": "arn:aws:iam::*:user/${aws:username}"
        },
        {
            "Sid": "BasicUser",
            "Effect": "Allow",
            "Action": [
                "iam:GetAccountSummary",
                "iam:GetAccountPasswordPolicy",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:GetServiceLinkedRoleDeletionStatus",
                "iam:ListAccountAliases",
                "iam:ListAttachedRolePolicies",
                "iam:ListPolicies",
                "iam:ListPolicyVersions",
                "iam:ListRolePolicies",
                "iam:ListRoles",
                "iam:ListRoleTags",
                "iam:ListVirtualMFADevices"
            ],
            "Resource": "*"
        },
        {
            "Sid": "PowerUser",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:UpdateRole",
                "iam:PassRole",
                "iam:TagRole",
                "iam:UntagRole",
                "iam:AttachRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy",
                "iam:UpdateAssumeRolePolicy",
                "iam:CreateServiceLinkedRole",
                "iam:DeleteServiceLinkedRole",
                "iam:PutRolePermissionsBoundary",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:DeleteRolePermissionsBoundary",
                "iam:AddRoleToInstanceProfile",
                "iam:UpdateRoleDescription",
                "iam:ListInstanceProfilesForRole",
                "iam:CreateInstanceProfile",
                "iam:DeleteInstanceProfile",
                "iam:GetInstanceProfile",
                "iam:ListInstanceProfiles"
            ],
            "Resource": "*"
        },
        {
            "Sid": "LimitedAdmin",
            "Effect": "Allow",
            "Action": [
                "iam:AddUserToGroup",
                "iam:CreateGroup",
                "iam:DeleteGroup",
                "iam:UpdateGroup",
                "iam:AttachGroupPolicy",
                "iam:DeleteGroupPolicy",
                "iam:DetachGroupPolicy",
                "iam:PutGroupPolicy",
                "iam:RemoveUserFromGroup",
                "iam:AttachUserPolicy",
                "iam:CreateUser",
                "iam:DeleteUser",
                "iam:UpdateUser",
                "iam:DeleteUserPolicy",
                "iam:DetachUserPolicy",
                "iam:PutUserPolicy",
                "iam:GetGroup",
                "iam:GetGroupPolicy",
                "iam:ListGroups",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupsForUser",
                "iam:ListGroupPolicies",
                "iam:GetUser",
                "iam:GetUserPolicy",
                "iam:ListUsers",
                "iam:ListUserPolicies",
                "iam:ListAttachedUserPolicies",
                "iam:ListServerCertificates",
                "iam:GenerateServiceLastAccessedDetails",
                "iam:SimulateCustomPolicy",
                "iam:SimulatePrincipalPolicy",
                "iam:GetAccountAuthorizationDetails",
                "iam:GetCredentialReport",
                "iam:GetServerCertificate",
                "iam:GetSAMLProvider",
                "iam:ListSAMLProviders",
                "iam:ListEntitiesForPolicy",
                "iam:ListPoliciesGrantingServiceAccess",
                "iam:GetServiceLastAccessedDetails",
                "iam:GetLoginProfile",
                "iam:SetSecurityTokenServicePreferences",
                "iam:TagUser",
                "iam:UntagUser",
                "iam:ListUserTags",
                "iam:PutUserPermissionsBoundary",
                "iam:GenerateOrganizationsAccessReport",
                "iam:GetOrganizationsAccessReport"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AccountSpecialist",
            "Effect": "Deny",
            "Action": [
                "ds:*",
                "sso-directory:*",
                "cognito-identity:*",
                "cognito-idp:*",
                "cognito-sync:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SecretsSpecialist",
            "Effect": "Deny",
            "Action": [
                "acm:*",
                "cloudhsm:*",
                "kms:*",
                "ram:*",
                "secretsmanager:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SecuritySpecialist",
            "Effect": "Deny",
            "Action": [
                "guardduty:*",
                "inspector:*",
                "macie:*",
                "securityhub:*",
                "waf:*",
                "waf-regional:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Admin",
            "Effect": "Deny",
            "Action": [
                "aws-portal:*PaymentMethods",
                "budgets:ModifyBudget",
                "s3:GetBucketPublicAccessBlock",
                "s3:PutBucketPublicAccessBlock",
                "s3:GetAccountPublicAccessBlock",
                "s3:PutAccountPublicAccessBlock",
                "iam:CreatePolicy",
                "iam:DeletePolicy",
                "iam:CreateAccountAlias",
                "iam:DeleteAccountAlias",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:SetDefaultPolicyVersion",
                "iam:CreateLoginProfile",
                "iam:UpdateLoginProfile",
                "iam:DeleteLoginProfile",
                "iam:UpdateAccountPasswordPolicy",
                "iam:DeleteAccountPasswordPolicy",
                "iam:UpdateServerCertificate",
                "iam:UploadServerCertificate",
                "iam:DeleteServerCertificate",
                "iam:ListOpenIDConnectProviders",
                "iam:GetOpenIDConnectProvider",
                "iam:AddClientIDToOpenIDConnectProvider",
                "iam:CreateOpenIDConnectProvider",
                "iam:UpdateOpenIDConnectProviderThumbprint",
                "iam:DeleteOpenIDConnectProvider",
                "iam:RemoveClientIDFromOpenIDConnectProvider",
                "iam:CreateSAMLProvider",
                "iam:UpdateSAMLProvider",
                "iam:DeleteSAMLProvider",
                "iam:GetContextKeysForCustomPolicy",
                "iam:GetContextKeysForPrincipalPolicy",
                "iam:GenerateCredentialReport",
                "iam:GetServiceLastAccessedDetailsWithEntities",
                "iam:DeleteUserPermissionsBoundary"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EditAdmin",
            "Effect": "Deny",
            "Action": [
                "iam:*"
            ],
            "Resource": "arn:aws:iam::*:user/admin"
        },
        {
            "Sid": "UseAdminPolicy",
            "Effect": "Deny",
            "Action": [
                "iam:*"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "iam:PolicyArn": [
                        "arn:aws:iam::[YOUR ACCOUNT ID]:group/Admin",
                        "arn:aws:iam::[YOUR ACCOUNT ID]:role/Admin",
                        "arn:aws:iam::[YOUR ACCOUNT ID]:policy/IAM-LimitedAdmin",
                        "arn:aws:iam::aws:policy/AdministratorAccess",
                        "arn:aws:iam::aws:policy/IAMFullAccess",
                        "arn:aws:iam::aws:policy/SystemAdministrator"
                    ]
                }
            }
        }
    ]
}
```