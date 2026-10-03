# Architecture

```text
                    +----------------------+
                    | ServiceNow User      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | ACL evaluation        |
                    +----------+-----------+
                               |
          +--------------------+--------------------+
          |                    |                    |
          v                    v                    v
      READ / bb1          CREATE / bb2         WRITE / bb3
          |                    |                    |
          |                    |                    |
          +---------+----------+--------------------+
                    |
                    v
           u_institution_details
                    |
                    v
              DELETE / bb4

READ also has:
Branch is EEE
Admin bypass in script
```

The READ path is the only path in the supplied specification that includes an advanced script and the `Branch is EEE` data condition.

The CREATE, WRITE and DELETE ACLs are role-based ACL records without a supplied script.
