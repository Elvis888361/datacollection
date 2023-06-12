import frappe

@frappe.whitelist(allow_guest=True)
def create_premium_client_details(fname,email,country,city):
    print(f"\n\n{fname}")

    insert_contact_details=frappe.get_doc({
        "doctype":"premiumClientsDetails",
        "full_name":fname,
        "email":email,
        "country":country,
        "city":city
    })
    insert_contact_details.insert(ignore_permissions=True)
    frappe.db.commit()
@frappe.whitelist(allow_guest=True)
def create_premium_server_details(bench,email,address,password,site):
    insert_contact_details=frappe.get_doc({
        "doctype":"premiumServerDetails",
        "user_name":bench,
        "email":email,
        "server_ip_address":address,
        "remote_password":password,
        "site_url":site
    })
    insert_contact_details.insert(ignore_permissions=True)
    frappe.db.commit()