class Call(object):
    def __init__(self, id, name, phone_number, time_of_call, reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time_of_call = time_of_call
        self.reason = reason

    def print_info(self):
        print "The call received at", str(self.time_of_call), "from", str(self.name), "at", str(self.phone_number), "was because", str(self.reason), ". We have given this call a unique ID of", str(self.id)


Rob = Call("Rob Lowe", "Larry", "555-5555", "11:34pm", "Lowe's is getting robbed")      
Rob.print_info()  

