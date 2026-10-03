# Deployment Guide

## 1. Create the user

In ServiceNow:

1. Log in with admin access.
2. Navigate to **User Administration → Users**.
3. Create the test user:
   - User ID: `EEE User`
   - First name: `EEE`
   - Last name: `User`
   - Email: `eeeuser@gmail.com`

## 2. Create roles

Navigate to **User Administration → Roles** and create:

- `bb1`
- `bb2`
- `bb3`
- `bb4`

Assign all four roles to the EEE test user for full workflow verification.

## 3. Create the table

Navigate to **System Definition → Tables**.

Create:

- Label: `Institution Details`
- Name: `u_institution_details`
- Extends: false

Add the fields documented in `config/table-schema.json`.

## 4. Add test records

Create records with `Branch` values:

- EEE
- ECE
- CSE

The CSV in `sample-data/institution-details.csv` is a sample dataset for manual population.

## 5. Create the READ ACL

Navigate to **System Security → Access Control (ACL)** and elevate the `security_admin` role.

Create:

- Type: `record`
- Operation: `read`
- Name: `u_institution_details`
- Active: `true`
- Advanced: `true`
- Required role: `bb1`
- Data condition: `Branch is EEE`

Paste the contents of `src/acl/read_acl.js` into the Script field.

## 6. Create CREATE, WRITE and DELETE ACLs

Use the configuration in `config/acls.json` and the individual files under `src/acl/`.

## 7. Verification

Use `docs/verification.md` and `tests/access-matrix.md`.

## Important

The supplied project describes the ServiceNow UI configuration but does not provide a native update-set XML export. Therefore this repository intentionally provides reproducible source/configuration and deployment instructions rather than claiming to be a one-click import package.
