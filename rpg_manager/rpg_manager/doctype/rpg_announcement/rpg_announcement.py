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

    def on_delete(self):
            frappe.msgprint('перед удалением!')

    def before_delete(self):
        # Показываем сообщение о запуске метода
        frappe.msgprint(f"Triggered before_delete for {self.name}")
        
        # Получаем все связанные игры, которые ссылаются на данный анонс
        related_games = frappe.get_all("Rpg Game", filters={"announcement": self.name}, fields=["name"])
        
        # Показываем сообщение с количеством найденных связанных игр
        frappe.msgprint(f"Related games found: {len(related_games)}")
        
        # Удаляем связанные игры
        for game in related_games:
            frappe.msgprint(f"Deleting game: {game['name']}")
            frappe.delete_doc("Rpg Game", game['name'], force=True)


