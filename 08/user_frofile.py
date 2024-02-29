def bulid_profile(first, last, **user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile = bulid_profile('kim', 'seyoung', location='pnu', field='cs', tall=173)
print(user_profile)