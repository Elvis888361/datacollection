# Copyright (c) 2023, data and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import subprocess
import requests
import shutil
import os
import secrets

class premiumServerDetails(Document):
	pass
@frappe.whitelist()
def work(bench, site,server_ip_address,email,name):
	remote_script_path = '/home/install_script.sh'
	adminpassword = secrets.token_hex(16)
	sqlpasswords = secrets.token_hex(16)
	command = f'sshpass -p FZpDH4swK0TBWiw ssh -o StrictHostKeyChecking=no root@159.89.103.194 "bash {remote_script_path} {adminpassword} {sqlpasswords} {site}"'
	sshpass_command = f'sshpass -p C9ALLQ5D1vw4g9Y ssh -o StrictHostKeyChecking=no root@159.89.103.194 "{command}"'
	process = subprocess.run(sshpass_command, shell=True, capture_output=True)
	if process.returncode == 0:
		frappe.msgprint(f"{site} Created successfully.")
		frappe.db.set_value('premiumServerDetails',name,'status','created')
		try:
			greatings=f"Dear {bench},<br/><br/>"
			message="We are pleased to inform you that Upeosoft Application has successfully created an instance of ERPNext for you.</b> Please find below the login credentials for your new ERPNext instance:<br/><br/>"
			closing=f"<ul><li>Username:<b> {bench}</b> </li><li>Administartors Password:<b> {adminpassword}</b> </li><li>Mysql Password: <b>{sqlpasswords}</b> </li></ul><br/><br/>"
			closing2="Thank you for choosing Upeosoft Application. If you have any questions or concerns, please do not hesitate to contact us."
			regards="<br/><br/> Best regards,<br/><br/> The Upeosoft Application Team.<br/><br/>"
			Body=greatings+message+closing+closing2+regards
			frappe.sendmail(
					recipients = email,
					cc = '',
					subject = "ERPNext Successfully Created",
					content = Body,
					reference_doctype = '',
					reference_name = '',
					now = True
				)
			
		except:
			frappe.msgprint("Could not send the Rejected Email")
	else:
		error_message = process.stderr.decode().strip() if process.stderr else "Unknown error occurred."
		frappe.msgprint(f"Shell command failed: {error_message}")
		frappe.msgprint(f"{site} not Created successfully.")
