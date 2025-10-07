# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SoftwareAssets(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.model.document import Document
		from frappe.types import DF

		additional_notes: DF.SmallText | None
		auth: DF.Literal["Login", "License Key"]
		covenant: DF.Attach | None
		images: DF.AttachImage | None
		invoice: DF.Attach | None
		invoices: DF.Attach | None
		license_key: DF.Data | None
		login_password: DF.Password | None
		login_username: DF.Data | None
		manufacturer: DF.Link | None
		model: DF.Data
		renew_cycle: DF.Literal["Monthly", "Every 3 Months", "Every 6 Months", "Yearly", "Permanent"]
		service: DF.Link
		state: DF.Literal["Active", "Inactive", "Expired"]
		subscription_expires: DF.Datetime | None
		table_gqjh: DF.Table[Document]
	# end: auto-generated types
	pass
