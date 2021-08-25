import frappe
import frappe.defaults
import frappe.permissions
from frappe.model.document import Document
from frappe import throw, msgprint
from frappe.utils import escape_html


# API For This Method
# http://0.0.0.0:8005/api/method/walk_in.walk_in.api.walk_in.walk

@frappe.whitelist(allow_guest=True)
def walk(applicant_name, email_id, address, source):
    job_appl = frappe.new_doc("Job Applicant")
    job_appl.applicant_name = applicant_name
    job_appl.email_id = email_id
    job_appl.address = address
    job_appl.source = source
    
    job_appl.save(ignore_permissions=True)
    return "Walk_In Successfully Signed-Up"