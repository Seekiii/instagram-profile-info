import requests
import json

def user_info(data):
	user = data['user']
	localData = {
		"bio":user['biography'],
		"links":user['bio_links'],
		"followers":user['edge_followed_by']['count'],
		"following":user['edge_follow']['count'],
		"name":user['full_name'],
		"avatar":user['profile_pic_url_hd'],
		"username":user['username'],
		"private":user['is_private'],
		"verified":user['is_verified'],
		"bussines":user['is_business_account'],
		"bussiness_email":user['business_email'],
		"bussines_phone":user['business_phone_number'],
		"business_category_name":user['business_category_name'],
		"category_name":user['category_name'],
	}
	posts = []
	profiles = []
	for post in user['edge_owner_to_timeline_media']['edges']:
		post = post['node']
		posts.append({
			"dimensions":post['dimensions'],
			"url":post['display_url'],
			"video":post['is_video'],
			"desc":post['edge_media_to_caption']['edges'][0]['node']['text'],
			"code":post['shortcode'],
			"comments_num":post['edge_media_to_comment'],
			"comments_disabled":post['comments_disabled'],
			"likes":post['edge_liked_by']
		})
	localData['posts'] = posts

	for profile in user['edge_related_profiles']['edges']:
		profile = profile['node']
		profiles.append({
			"name":profile['full_name'],
			"private":profile['is_private'],
			"verified":profile['is_verified'],
			"avatar":profile['profile_pic_url'],
			"username":profile['username']
		})
	localData['related_profiles'] = profiles
	return localData

def get_info(username):
	url = f"https://www.instagram.com/{username}/?__a=1&__d=1"
	r = requests.get(url)
	data = r.json()['graphql']
	info = user_info(data)
	return info



user = get_info("nugato")

print(json.dumps(user,indent=4))