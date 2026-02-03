import firebase_admin
from firebase_admin import credentials, firestore
from mcp.server.fastmcp import FastMCP
import mcp
cred = credentials.Certificate("./service.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref= store.collection(u'users')

# docs = doc_ref.get()
# for doc in docs:
#     print(u'Doc Data:{}'.format(doc.to_dict()))

@mcp.tool()
def get_users():
    users = []
    docs = doc_ref.get()
    for doc in docs:
        users.append(doc.to_dict())
    return users

@mcp.tool()
def get_appointments(id):
    appointments_ref = (
        store.collection("appointment")
          .where("userId", "==", id)
    )

    docs = appointments_ref.stream()
    return [doc.to_dict() for doc in docs]


user_id = "HxIQtiR6CBR8WaebSNajFfIi3853"
appointments = get_appointments(user_id)

print(appointments)