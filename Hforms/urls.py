def make_url(user,title):
	url = ''
	url += user.username
	url += '_'
	url += title
	return url

def get_url(url):
	username = ''
	title = ''
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