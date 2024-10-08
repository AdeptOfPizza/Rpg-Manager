# Copyright (c) 2024, roman zyryanov and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


#class RpgAnnouncement(Document):
#	def on_update(self):
#
#		if self.status1 == f'Full':
#			frappe.msgprint('it tracks!')
#		else:
#			frappe.msgprint('update!')

class RpgAnnouncement(Document):
    def on_update(self):
        if self.status1 == "Full" and not frappe.db.exists("Rpg Game", {"announcement": self.name}):
            new_game = frappe.get_doc({
                "doctype": "Rpg Game",
                "owner": self.owner,
                "announcement": self.name,
                "players": self.current_players
            })
            new_game.insert()


