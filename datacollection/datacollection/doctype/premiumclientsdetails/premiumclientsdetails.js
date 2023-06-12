// Copyright (c) 2023, data and contributors
// For license information, please see license.txt

frappe.ui.form.on('premiumClientsDetails', {
	refresh: function(frm) {
		frm.add_custom_button(__('Create ErpNext'), function(){
			frappe.call({
				method: 'datacollection.datacollection.doctype.premiumclientsdetails.premiumclientsdetails.work',
				args: {
					'bench':frm.doc.full_name,
					'email':frm.doc.email,
					'name':frm.doc.name
				},
				callback: function(r) {
					
				}
			});
		}, __("Action"));
	}
});
