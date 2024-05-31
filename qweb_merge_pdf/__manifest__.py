{
    "name": "PDF Merger",
    "version": "17.0.1.0.0",
    "summary": "Merge the different pdfs with report by language. So for example,"
    "for Quotation/Order report, if user attached 3 different pdfs with English,"
    "German and Maxico language and user print report with customer that have"
    "German language in its profile, then system automatic attach German"
    "language pdf to the report.",
    # Author
    "author": "Synodica Solutions Pvt. Ltd.",
    "website": "https://synodica.com",
    "maintainer": "Synodica Solutions Pvt. Ltd.",
    "depends": ["base"],
    "images": ["static/description/qweb_pdf_banner.gif"],
    "data": ["security/ir.model.access.csv", "views/ir_action_report.xml"],
    "installable": True,
    "license": "LGPL-3",
}
