people = {1: {"nama": "arsene lupin", "nik": "1234", "jenis_kelamin": "male", "tanggal_lahir": "1902-03-23"},
          2: {"nama": "sherlock holmes", "nik": "4321", "jenis_kelamin": "male", "tanggal_lahir": "1876-08-16"},
          3: {"nama": "irene adler", "nik": "6789", "jenis_kelamin": "female", "tanggal_lahir": "1884-10-07"}}

nama = input('Nama? :')
for key, value in people.items():
    if people[key]['nama'] == nama:
        print(value)

    else:
        print('data tak ada')
