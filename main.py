import firebase_admin
from firebase_admin import credentials, firestore
from mcp.server.fastmcp import FastMCP
import  os
cred = credentials.Certificate("service.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref= store.collection(u'users')
PORT = os.environ.get("PORT", 8000)

mcp = FastMCP("docs", host='0.0.0.0', port=PORT)

# docs = doc_ref.get()
# for doc in docs:
#     print(u'Doc Data:{}'.format(doc.to_dict()))

@mcp.tool()
def get_users():

    """
    This tool will fetch all the users from the database
    """
    users = []
    docs = doc_ref.get()
    for doc in docs:
        users.append(doc.to_dict())
    return users

@mcp.tool()
def get_appointments(id):
    """
    Docstring for get_appointments
    
    :param id: userId for which to fetch appointments
    :return: List of appointments for the given userId
    """
    appointments_ref = (
        store.collection("appointment")
          .where("userId", "==", id)
    )

    docs = appointments_ref.stream()
    return [doc.to_dict() for doc in docs]


# user_id = "HxIQtiR6CBR8WaebSNajFfIi3853"
# appointments = get_appointments(user_id)

# print(appointments)
if __name__ == "__main__":
    mcp.run(transport="stdio")