import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("jet-lag-lamp-firebase-adminsdk-0rh7f-6066be5715.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'Developers').document(u'uuuu')
doc_ref.set({
    u'name': "cello",
    u'age': "21",
})