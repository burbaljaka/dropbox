import requests
import dropbox
import posixpath

#
# dbx = dropbox.Dropbox(oauth2_access_token="mr9dY_ILp_AAAAAAAAAAmmmOjuR54lE9k1TekGgxZxSMycdQS9uyRhzr01yLJWa8")
# result1 = dbx.files_list_folder(path="")
# print(result1.entries)
# result2 = dbx.files_list_folder(path=result1.entries[0].path_lower)
# # print(result2.entries)
# result3 = dbx.files_list_folder(path=result2.entries[0].path_lower)
# # print(result3.entries)
#
# result4  = dbx.files_list_folder_get_latest_cursor(path=result2.entries[0].path_lower)
# # print(result4.cursor)

# Загрузка файла:
# with open('Договор Капитонов ИП (2).docx', 'rb') as f:
#     content = f.read()
#     filename = f.name
#
# path=posixpath.join('', filename)
# print(path)
#
# result5 = dbx.files_upload(path='/'+filename, f=content)
# print(result5)

# result = dbx.cloud_docs_get_content('id:XBRW9Dk-b6AAAAAAAAAAFQ', )
# print(result)


url = 'https://www.dropbox.com/oauth2/authorize?client_id={}&response_type=code'.format('lalonondqj6ycpa')

response = requests.get(url)
print(response.text)




