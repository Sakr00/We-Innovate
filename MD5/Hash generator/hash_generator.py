import hashlib
#hash define
md5 = hashlib.md5() #000101001+2 dofgj ==> 010101001+2 01010001110 ==> hexa  
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 = hashlib.sha512()
list_hash_objects = [md5, sha1, sha224, sha256, sha384 , sha512]
def hash_string(palin_text):
    for hash_object in list_hash_objects:
            hash_object.update(plain_text.encode('utf-8'))
            print('{}:{}'.format(hash_object.name , hash_object.hexdigest()))

def hash_file(path):
    for hash_object in list_hash_objects:
        with open(path , 'rb') as opened :
            for line in opened:
                hash_object.update(line)
            print('{}:{}'.format(hash_object.name , hash_object.hexdigest()))

def md5_string(plain_text):
    md5.update(plain_text.encode('utf-8'))
    res = md5.hexdigest()
    return res
print("For files choose 1  For strings choose 2 For MD5 string choose 3 For file string by string choose 4 ")
user_input = input("Enter your choice: ")
if user_input == '1':
    path = input("Enter the file path: ")
    hash_file(path=path)
elif user_input == '2' :
    plain_text = input("Enter the plain text: ")
    hash_string(palin_text=plain_text)
elif user_input == '3' :
    plain_text = input("Enter the plain text: ")
    restult = md5_string(plain_text= plain_text)
    print(restult)
elif user_input == '4' :
    path = input("Enter the file path: ")
    for line in open(path):
        result = md5_string(plain_text= line)
        appendFile = open('new.txt','a')
        appendFile.write(result + '\n')

appendFile.close()