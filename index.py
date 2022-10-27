
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate("progetto-4df6c-firebase-adminsdk-yvbpa-058ff8a8dd.json")
app = firebase_admin.initialize_app(cred)


#Application Default credentials are automatically created
db = firestore.client()

users_ref = db.collection('utenti')
docs = users_ref.stream()

doc_ref = db.collection('utenti').document('UUUUUUU7777UUUUUU')
doc_ref.set({
    'nome': 'Ada',
    'cognome': 'Lovelace',
    'born': 1815
})


for doc in docs:
    if 'nome' in doc.to_dict():
    #print(f'{doc.id} => {doc.to_dict()}') -- per stampare tutto
        print(doc.to_dict()['nome'])

print('--------------')



cities_ref = db.collection("utenti")
query = cities_ref.order_by("nome").limit(3)
results = query.get()

for doc in results:
    print(doc.to_dict()['nome'])


