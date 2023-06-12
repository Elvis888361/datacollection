// Copyright (c) 2023, data and contributors
// For license information, please see license.txt

frappe.ui.form.on('premiumServerDetails', {
	refresh: function(frm) {
		frm.add_custom_button(__('Create ErpNext'), function(){
			frappe.call({
				method: 'datacollection.datacollection.doctype.premiumserverdetails.premiumserverdetails.work',
				args: {
					'bench':frm.doc.user_name,
					'site':frm.doc.site_url,
					'server_ip_address':frm.doc.server_ip_address,
					'remote_password':frm.doc.remote_password,
					'email':frm.doc.email,
					'name':frm.doc.name
				},
				callback: function(r) {
					
				}
			});
		}, __("Action"));
	}
});
