from transitions.extensions import GraphMachine
from utils import send_image_url,send_text_message

int value

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_info(self, event):
        text = event.message.text
        return text.lower() == "info"

    def is_going_to_income(self, event):
        text = event.message.text
        return text.lower() == "income:" #+value

    def is_going_to_expense(self, event):
        text = event.message.text
        return text.lower() == "expense:" #+value  

    def is_going_to_balance(self, event):
        text = event.message.text
        return text.lower() == "balance?"     

    def on_enter_info(self, event):
        print("I'm entering info state")
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter:\n\"Income:(value)\" for inputting income\n\"Expense:(value)\" for inputting expense\n\"Balance?\" for inputting income")
        self.go_back()

    def on_exit_info(self):
        print("Leaving info state")

    def on_enter_income(self, event):
        print("I'm entering income state")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"Income:(value)\" ")
        self.go_back()

    def on_exit_income(self):
        print("Leaving income state")

    def on_enter_expense(self, event):
        print("I'm entering expense")
        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger expense")
        message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTofOKxN6YUlx8zEPGMpRxI1vRmpDxZzgHy4QVr4KIXMBk38Avb',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTofOKxN6YUlx8zEPGMpRxI1vRmpDxZzgHy4QVr4KIXMBk38Avb'
        )
        line_bot_api.reply_message(event.reply_token, message)
        #send_image_url(,"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTofOKxN6YUlx8zEPGMpRxI1vRmpDxZzgHy4QVr4KIXMBk38Avb")
        self.go_back()

    def on_exit_expense(self):
        print("Leaving expense")
    


    def on_enter_balance(self, event):
        print("I'm entering balance")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger balance")
        self.go_back()

    def on_exit_balance(self):
        print("Leaving balance")