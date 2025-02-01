# import pyrebase


# def noquote(s):
#     return s
# pyrebase.pyrebase.quote = noquote


# def fetch_last(db, collection, n=20):
#     objects = db.child(collection).order_by_key().limit_to_last(n).get()
#     return objects


def fetch_last(db, collection, n=20):
    try:
        objects = db.child(collection).order_by_key().limit_to_last(n).get()
        return objects
    except Exception as e:
        print(f"Error fetching data from Firebase: {e}")
        return None

