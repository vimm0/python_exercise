

class messageUser():
	names=[]
	user_detail=[]
	# name=''
	base_messages="""
	Hello, {name}
		I'm here to inform you that course {faculty}
		you are trying to apply is available
		please arrive college in time for further
		negotiation.
								Thankyou!!
								Sandesh Rana
								co-1ordinator
	"""

	def add_user(self, name,faculty):
		name = name[0].upper()+name[1:].lower()
		faculty=faculty
		detail={
		"name":name,
		"faculty":faculty
		}
		self.user_detail.append(detail)

	def detail_object(self):
		return self.user_detail

	def make_message(self):
		if len(self.user_detail)>0:
			for detail in self.detail_object():
				name=detail['name']
				faculty=detail['faculty']
				message=self.base_messages 
				new_msg=message.format(name=name,faculty=faculty)
			return new_msg
		return []
