# Script-Controlled ACL – Restrict Record Access Based on Field Value

A GitHub-ready ServiceNow project based on the supplied lab specification.

## Project objective

Restrict access to records in the `u_institution_details` table based on the `Branch` field and user roles.

The supplied project specifies:

- Custom table: `u_institution_details`
- Branch choices: `ECE`, `EEE`, `CSE`
- Custom roles: `bb1`, `bb2`, `bb3`, `bb4`
- READ: `bb1`
- CREATE: `bb2`
- WRITE: `bb3`
- DELETE: `bb4`
- Administrators retain full access
- The READ ACL includes the data condition `Branch is EEE`

The original lab's READ ACL script is preserved in `src/acl/read_acl.js`.

> Important: this repository is a source/configuration package for implementing the lab in ServiceNow. It is not represented as a native ServiceNow application/update-set export because the supplied source did not contain a real ServiceNow update-set export.

## Repository structure

```text
Script-Controlled-ACL-ServiceNow/
├── README.md
├── .gitignore
├── LICENSE
├── config/
│   ├── acls.json
│   ├── roles.json
│   └── table-schema.json
├── docs/
│   ├── architecture.md
│   ├── deployment.md
│   └── verification.md
├── sample-data/
│   └── institution-details.csv
├── src/
│   └── acl/
│       ├── read_acl.js
│       ├── create_acl.md
│       ├── write_acl.md
│       └── delete_acl.md
├── tests/
│   └── access-matrix.md
└── scripts/
    └── validate_config.py
```

## Implementation summary

### Table

`u_institution_details`

Fields:

- Student Roll Number — Auto Number
- Student Name — Reference to User
- Faculty Name — Reference to User
- Branch — Choice (`ECE`, `EEE`, `CSE`)
- Email — String
- Phone Number — String
- Description — Multi String

### READ ACL

- Type: `record`
- Operation: `read`
- Name: `u_institution_details`
- Active: `true`
- Required role: `bb1`
- Data condition: `Branch is EEE`
- Advanced script: see `src/acl/read_acl.js`

### CREATE ACL

- Type: `record`
- Operation: `create`
- Name: `u_institution_details`
- Active: `true`
- Required role: `bb2`
- No data condition

### WRITE ACL

- Type: `record`
- Operation: `write`
- Name: `u_institution_details`
- Active: `true`
- Required role: `bb3`
- No data condition

### DELETE ACL

- Type: `record`
- Operation: `delete`
- Name: `u_institution_details`
- Active: `true`
- Required role: `bb4`
- No data condition

## Deployment

Follow `docs/deployment.md`.

## Verification

Follow `docs/verification.md` and `tests/access-matrix.md`.

## Source fidelity

The repository intentionally preserves the supplied lab's terminology and READ script. Any implementation hardening or deviation should be made explicitly and documented rather than silently changing the supplied project.
