import frappe

#@frappe.whitelist()
#def fetch(document):
#    game = frappe.get_doc("Rpg Game", document)
#    announcement = frappe.get_doc("Rpg Announcement", game.announcement)
 #   game.current_players = announcement.current_players
 #   game.save()



from frappe.desk.doctype.notification_log.notification_log import (
	enqueue_create_notification,
	get_title,
	get_title_html,
)

def send_notification_to_all():
    # Получаем всех активных пользователей системы, кроме системных и гостевых
    users = frappe.get_all("User", 
                           filters={"enabled": 1, "user_type": ["!=", "System User"], "name": ["!=", "Guest"]}, 
                           fields=["name"])

    # Отправляем уведомление каждому пользователю
    for user in users:
        enqueue_create_notification(
            user=user.name,
            subject="Тестовое уведомление",
            message="Сработало!")
