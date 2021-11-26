import random



P = random.randint(0,100)
G = random.randint(0,100)

alice_key = random.randint(0,100)
bob_key = random.randint(0,100)

print("Алиса сгенерировла приватный ключ: \t", alice_key)
print("Боб сгенерировал приватный ключ: \t", bob_key)

new_key_Alice = int(pow(G, alice_key, P))
new_key_Bob = int(pow(G, bob_key, P))

print("Новый ключ Алисы: \t", new_key_Alice)
print("Новый ключ Боба: \t", new_key_Alice)

sync_key_Alice = int(pow(new_key_Bob,alice_key,P))
sync_key_Bob = int(pow(new_key_Alice,bob_key,P))

if sync_key_Alice == sync_key_Bob:print(sync_key_Alice, sync_key_Bob)
