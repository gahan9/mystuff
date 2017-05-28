import hashlib
import random

# pool = ['SHA', 'DSA-SHA', 'MD5', 'md4', 'md5', 'RIPEMD160', 'ripemd160', 'SHA512', 'sha1', 'ecdsa-with-SHA1', 'sha256', 'DSA', 'SHA384', 'SHA1', 'whirlpool', 'SHA224', 'MD4', 'dsaWithSHA', 'sha224', 'sha512', 'dsaEncryption', 'sha384', 'SHA256', 'sha']
# fun_pool = [hashlib.SHA, hashlib.DSA-SHA, hashlib.MD5, hashlib.md4, hashlib.md5, hashlib.RIPEMD160, hashlib.ripemd160, hashlib.SHA512, hashlib.sha1, hashlib.ecdsa-with-SHA1, hashlib.sha256, hashlib.DSA, hashlib.SHA384, hashlib.SHA1, hashlib.whirlpool, hashlib.SHA224, hashlib.MD4, hashlib.dsaWithSHA, hashlib.sha224, hashlib.sha512, hashlib.dsaEncryption, hashlib.sha384, hashlib.SHA256, hashlib.sha]
# hash_function_pool_dict = {<built-in function openssl_sha512>: '041d06d6bafd942572b3278820cc2fabe1453176', <built-in function openssl_sha1>: '70c4507e8bafa12987aa3a24ca4c7b1a06342e0c', <built-in function openssl_sha384>: 'f0bcc2cedf10f422e308202d5d62f3bc8a5a2651', <built-in function openssl_md5>: '85af91576569f9a969ddefb772a1bdcca5180f9f', <built-in function openssl_sha256>: '0957512e40c457508dfbb4dc53a3ba97240c3f8c', <built-in function openssl_sha224>: '85779fea94a611490a0642fdbddd8b851118c0dc'}
# hash_pool_dict = {'SHA256': 'b92e713b21b29946a52e5ffe714c82eb670e98f9', 'SHA512': '42cc065f07e499226ac12f2671f652acfdaf3d73', 'dsaWithSHA': 'd99017b8dfb72e0f68367ac9e323e72b7af67156', 'md4': '136755d08fec0ed8df793cbc3bdf35b7fba8b127', 'sha256': 'b310da45b1ebf444106a41b7832ab2fbe25dab41', 'sha512': '0f5b530255e5a064cc73699e4fa44ba8b2ad399f', 'ripemd160': '453c7f4f8e131b7222d28b69e0207049cc8f454d', 'md5': 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b', 'whirlpool': '8650c1723c7bcc41e48f9a2077b8c630670a6978', 'SHA1': 'e1744a525099d9a53c0460ef9cb7ab0e4c4fc939', 'SHA224': '3660bf7dffee2749bbb0651a163dd732c562da7b', 'SHA': '9faed964fef80190696bb2b0b98ed45cb7120c93', 'SHA384': '5ab8fb3ba84c84c0b9929fd9b6d13f639d3078bb', 'ecdsa-with-SHA1': '53a5d70ca0646866563a4e0f680aef19bca59f26', 'MD4': '86e9fff1d00c68995ba96d3b00b707d9685f6995', 'DSA': '3dbf83ff89b0bb283ced3c1e49b246ab5743b7c5', 'sha1': '415ab40ae9b7cc4e66d6769cb2c08106e8293b48', 'DSA-SHA': 'ae14508918c893329fc0336bd97fa3595bf3016a', 'sha224': '9833c6130c3761726294923e9d575cbc7749da54', 'dsaEncryption': '21a5ea2153823a88c0fa201ec3d258ffaf6aef91', 'RIPEMD160': 'b40d6cd4cf673ac976eca2909907795c34bc177e', 'sha': 'd8f4590320e1343a915b6394170650a8f35d6926', 'MD5': 'b773bed04a48de200b96981bb79467413a222066', 'sha384': '1d3c8bcc44b8a2cba4c63b30774bf6644d4649c4'}
"""
{<built-in function openssl_sha512>: '041d06d6bafd942572b3278820cc2fabe1453176', 
<built-in function openssl_sha1>: '70c4507e8bafa12987aa3a24ca4c7b1a06342e0c', 
<built-in function openssl_sha384>: 'f0bcc2cedf10f422e308202d5d62f3bc8a5a2651', 
<built-in function openssl_md5>: '85af91576569f9a969ddefb772a1bdcca5180f9f', 
<built-in function openssl_sha256>: '0957512e40c457508dfbb4dc53a3ba97240c3f8c', 
<built-in function openssl_sha224>: '85779fea94a611490a0642fdbddd8b851118c0dc'} 
"""


class HybridHashGen(object):
    """
    
    """
    def random_hash_select(self):
        """
        
        :return: 
        """
        hash_pool = ['sha256', 'sha1', 'sha512', 'md5', 'sha384', 'sha224']
        function_pool = [hashlib.sha256, hashlib.sha1, hashlib.sha512, hashlib.md5, hashlib.sha384, hashlib.sha224]

        hash_function_pool_dict = {}
        for hash_name in function_pool:
            hash_function_pool_dict[hash_name] = hashlib.sha1(str(hash_name).encode('utf-8')).hexdigest()

        algo_to_encrypt_pass = random.choice(hash_function_pool_dict.keys())
        return [algo_to_encrypt_pass, hash_function_pool_dict]

    def generate_hash(self, hash_function, passwd='password'):
        """
        
        :param hash_function: 
        :param passwd: 
        :return: 
        """
        simple_pass = passwd
        pass_hash = hash_function(str(simple_pass).encode('utf-8')).hexdigest()
        return pass_hash


def hash_maker(passwd):
    """
    
    :param passwd: 
    :return: 
    """
    haybrid_hash_obj = HybridHashGen()
    random_hash = haybrid_hash_obj.random_hash_select()  # [<func>, {<fun>: 'hash'}]
    password_hash = haybrid_hash_obj.generate_hash(random_hash[0], passwd)
    final_hash = password_hash + random_hash[1].get(random_hash[0])
    # return random_hash[0], random_hash[1].get(random_hash[0])
    # return password_hash, final_hash, random_hash[1].get(random_hash[0])
    return final_hash


def hash_verifier(hashed_value):
    """
    
    :param hashed_value: 
    :return: 
    """
    function_pool = [hashlib.sha256, hashlib.sha1, hashlib.sha512, hashlib.md5, hashlib.sha384, hashlib.sha224]

    hash_function_pool_dict = {}
    for hash_name in function_pool:
        hash_function_pool_dict[hash_name] = hashlib.sha1(str(hash_name).encode('utf-8')).hexdigest()

    hashed_value = hashed_value
    hash_of_algo = hashed_value[-40:]
    hash_algo = hash_function_pool_dict.keys()[hash_function_pool_dict.values().index(hash_of_algo)]
    return hash_algo

hash_of_value = hash_maker('abc@12345')
print 'Hash value is : {}\n & \nHash algo is : {}'.format(hash_of_value, hash_of_value[-40:])

detected_hash = hash_verifier(hash_of_value)
print 'Hash is made from algo : ' + str(detected_hash)

