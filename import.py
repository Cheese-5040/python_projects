import target_store

target_store.init_program()
request = [[ '6076f6ccddc1145c187de178', 4,6,'kg', 'Mongkok','dairy'],[ '6076f6b8ddc1145c187de177', 0,1,'discrete', 'Mongkok','fruit']]
result= target_store.get_target_and_store(request)
request2 = [[ '6076f6ccddc1145c187de178', 7,11,'discrete', 'Causeway Bay','seafood'],[ '6076f6b8ddc1145c187de177', 3,1,'discrete', 'Mongkok','dairy']]
result2= target_store.get_target_and_store(request2)

print("result : ", result)
print("result2 : ", result2)