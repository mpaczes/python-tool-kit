function confirm_delete() {
    delete_owner = confirm('Do you want to delete owner / vehicle ?')

    if (delete_owner) {
        return true
    } else {
        return false
    }
}