# ACL Access Matrix

| User state | READ | CREATE | WRITE | DELETE |
|---|---:|---:|---:|---:|
| No custom roles | Denied | Denied | Denied | Denied |
| `bb1` | Allowed for EEE records | Denied | Denied | Denied |
| `bb1 + bb2` | Allowed for EEE records | Allowed | Denied | Denied |
| `bb1 + bb2 + bb3` | Allowed for EEE records | Allowed | Allowed | Denied |
| `bb1 + bb2 + bb3 + bb4` | Allowed for EEE records | Allowed | Allowed | Allowed |
| `admin` | Full access | Full access | Full access | Full access |

This matrix reflects the intended verification sequence in the supplied lab specification.
