import frappe
import frappe.defaults
import frappe.permissions
from frappe.model.document import Document
from frappe import throw, msgprint
from frappe.utils import escape_html


# API For This Method
# http://0.0.0.0:8005/api/method/walk_in.walk_in.api.walk_in.walk

@frappe.whitelist(allow_guest=True)
def walk(applicant_name, email_id, address, source, phone_number, job_title, emergency_contact_no, pan_no, residence, date_of_birth, blood_group,
            marital_status, english, hindi, marathi, other, name1, address1, phone1, name2, address2, phone2, school_univ, qualification,
            year_of_passing, company_name, designation, total_experience):
    
    job_appl = frappe.new_doc("Job Applicant")
    job_appl.applicant_name = applicant_name
    job_appl.email_id = email_id
    job_appl.address = address
    job_appl.source = source
    job_appl.phone_number = phone_number
    job_appl.job_title = job_title
    job_appl.emergency_contact_no = emergency_contact_no
    job_appl.pan_no = pan_no
    job_appl.residence = residence
    job_appl.date_of_birth = date_of_birth
    job_appl.blood_group = blood_group
    job_appl.marital_status = marital_status
    job_appl.english = english
    job_appl.hindi = hindi
    job_appl.marathi = marathi
    job_appl.other = other
    
    job_appl.append('education', {
        'school_univ': school_univ,
        'qualification': qualification,
        'year_of_passing': year_of_passing,
    })
    
    job_appl.append('external_work_history', {
        'company_name': company_name,
        'designation': designation,
        'total_experience': total_experience,
    })
    
    job_appl.append('family_reference', {
        'name1': name1,
        'address1': address1,
        'phone1': phone1,
    })
    
    job_appl.append('corporate_reference', {
        'name2': name2,
        'address2': address2,
        'phone2': phone2,
    })
    
    job_appl.set_missing_values()
    job_appl.save(ignore_permissions=True)
    return "Walk-In Cadidate Successfully Signed-Up..!!"
