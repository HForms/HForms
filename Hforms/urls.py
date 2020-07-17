def make_url(user,title):
	url = ''
	url += user.username
	url += '_'
	url += title
	return url

def get_details(url):
	username = ''
	title = ''
	li = []
	for c in url:
		if(c == '_'):
			break
		else:
			username += c
	for c in url[len(username)+1:]:
		title += c
	li.append(username)
	li.append(title)
	return li