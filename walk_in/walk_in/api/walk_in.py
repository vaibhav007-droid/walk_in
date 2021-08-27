import frappe
import frappe.defaults
import frappe.permissions
from frappe.model.document import Document
from frappe import throw, msgprint
from frappe.utils import escape_html
import json

# API For This Method
# http://0.0.0.0:8005/api/method/walk_in.walk_in.api.walk_in.walk

# @frappe.whitelist(allow_guest=True)
# def walk(applicant_name, email_id, address, source, phone_number, job_title, emergency_contact_no, pan_no, residence, blood_group,
#          marital_status, english, hindi, marathi, other, school_univ, qualification,
#          year_of_passing):
@frappe.whitelist(allow_guest=True)
def walk(applicant_name, email_id, address, source, phone_number, job_title, emergency_contact_no,
         pan_no, residence, blood_group, marital_status, english, hindi, marathi, other, date_of_birth,
         education, work_history, family, corporate):
        
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
    
    #Load Date Into Json
    date = json.loads(date_of_birth)
    job_appl.date_of_birth = date.get('date_of_birth')
    
    job_appl.blood_group = blood_group
    job_appl.marital_status = marital_status
    job_appl.english = english
    job_appl.hindi = hindi
    job_appl.marathi = marathi
    job_appl.other = other

    # education = {"school_univ":school, "qualification":qualify,"year_of_passing":y_o_p}
    edu=json.loads(education)
    wh = json.loads(work_history)
    fam = json.loads(family)
    cor = json.loads(corporate)

    job_appl.append('education', {
        'school_univ': edu.get('school_univ'),
        'qualification': edu.get('qualification'),
        'year_of_passing': edu.get('year_of_passing'),
    })
    job_appl.append('external_work_history', {
        'company_name': wh.get('company_name'),
        'designation': wh.get('designation'),
        'total_experience': wh.get('total_experience'),
    })
    job_appl.append('family_reference', {
        'name1': fam.get('name1'),
        'address1': fam.get('address1'),
        'phone1': fam.get('phone1'),
    })
    job_appl.append('corporate_reference', {
        'name2': cor.get('name2'),
        'address2': cor.get('address2'),
        'phone2': cor.get('phone2'),
    })

    job_appl.save(ignore_permissions=True)
    frappe.db.commit()

    return "Walk-In Cadidate Successfully Signed-Up..!!"
