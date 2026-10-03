/*
 * ServiceNow Record READ ACL
 * Table: u_institution_details
 *
 * Configuration:
 *   Type: record
 *   Operation: read
 *   Required role: bb1
 *   Data condition: Branch is EEE
 *   Advanced: true
 *
 * This script is preserved from the supplied project specification.
 */
(function () {
    // Allow admin users full access
    if (gs.hasRole('admin')) {
        return true;
    }

    // Allow users with bb1 to pass the ACL.
    // The ACL's configured data condition restricts the record to Branch = EEE.
    if (gs.hasRole('bb1')) {
        return true;
    }

    // Deny access for all others
    return false;
})();
