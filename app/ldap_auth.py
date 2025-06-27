# app/ldap_auth.py
from ldap3 import Server, Connection, ALL, SIMPLE, SUBTREE

class LDAPAuthenticator:
    def __init__(self, server_url, base_dn):
        self.server = Server(server_url, get_info=ALL)
        self.base_dn = base_dn

    def authenticate(self, username, password):
        user_dn = f"cn={username},{self.base_dn}"
        try:
            conn = Connection(self.server, user=user_dn, password=password, authentication=SIMPLE)
            if conn.bind():
                # Check user role from attributes (mock logic, adjust based on your LDAP schema)
                role = "admin" if "admin" in username else "teacher"
                conn.unbind()
                return role
            return None
        except Exception as e:
            print(f"LDAP Authentication error: {e}")
            return None
