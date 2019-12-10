from transitions.extensions import GraphMachine
from utils import send_image_url,send_text_message,push_message

value = 0
sid = " "
eid = " "
ex = 0
inc = 0


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_info(self, event):
        text = event.message.text
        return text.lower() == "info"

    def is_going_to_income(self, event):
        text = event.message.text
        if (text.split(' ')[0]=="Income:") and (len(text.split(' '))==2):
            global sid
            global value
            global inc
            sid = text.split(' ')[1]
            inc = inc + int(sid)
            value = value + int(sid)
            text = text.split(' ')[0]
        return text.lower() == "income:"

    def is_going_to_expense(self, event):
        text = event.message.text
        if (text.split(' ')[0]=="Expense:") and (len(text.split(' '))==2):
            global eid
            global value
            global ex
            eid = text.split(' ')[1]
            ex = ex + int(eid)
            value = value - int(eid)
            text = text.split(' ')[0]
        return text.lower() == "expense:"  

    def is_going_to_balance(self, event):
        text = event.message.text
        return text.lower() == "balance?"     

    def on_enter_info(self, event):
        print("I'm entering info state")
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter:\n\"Income: (value)\" for inputting income\n\"Expense: (value)\" for inputting expense\n\"Balance?\" to check your current balance")
        self.go_back()

    def on_exit_info(self):
        print("Leaving info state")

    def on_enter_income(self, event):
        
        print("I'm entering income state")
        reply_token = event.reply_token
        send_text_message(reply_token, "Today's Income: " + str(inc))
        self.go_back()

    def on_exit_income(self):
        print("Leaving income state")

    def on_enter_expense(self, event):
        print("I'm entering expense")
        reply_token = event.reply_token
        push_message("U46b5bdcccc8124e05d79148943af39e5", "Today's Expense: " + str(ex))
        push_message("U46b5bdcccc8124e05d79148943af39e5", StickerSendMessage(package_id='11537',sticker_id='52002759'))
        self.go_back()

    def on_exit_expense(self):
        print("Leaving expense")
    


    def on_enter_balance(self, event):
        print("I'm entering balance")
        reply_token = event.reply_token
        push_message("U46b5bdcccc8124e05d79148943af39e5", "Current Balance: " + str(value))
        send_image_url("U46b5bdcccc8124e05d79148943af39e5","https://media.istockphoto.com/vectors/businessman-hands-holding-passbook-with-no-balance-vector-id482975000?k=6&m=482975000&s=612x612&w=0&h=0pkEu9sjfUePhycuuXb3FnIl0iFe5pDwKwdRWlL7V-0=")
        self.go_back()

    def on_exit_balance(self):
        print("Leaving balance")