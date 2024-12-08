#Игнатенко Александр, 24-когорта. Финальный проект. Инженер по тестированию плюс
import sender_stand_requests
import data

def assertion_code_200():
	response_pno = sender_stand_requests.post_new_order(data.order_body)
	track = response_pno.json()["track"]
	return sender_stand_requests.get_order_from_track(track).status_code

# Проверить, что код ответа равен 200.
def test_get_order_from_track_code_200():
	assert assertion_code_200() == data.status_code_200