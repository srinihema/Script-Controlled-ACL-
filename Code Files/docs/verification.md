# Verification Procedure

## READ

1. Impersonate the EEE user.
2. Open:
   `u_institution_details.list`
3. Verify that EEE records are visible according to the configured READ ACL.
4. Impersonate a user without `bb1` and verify that records are not accessible.
5. Impersonate an administrator and verify full access.

## CREATE

Verify that a user with `bb1` + `bb2` can use the New button and create a record, as described by the supplied project.

## WRITE

Verify that a user with `bb1` + `bb2` + `bb3` can edit records.

## DELETE

Verify that a user with `bb1` + `bb2` + `bb3` + `bb4` can delete records.

## Security note

The exact source project states that READ uses both a role requirement and a `Branch is EEE` data condition. Keep both configured when reproducing the lab.
