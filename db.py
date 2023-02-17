import json
#Create Like counting class
class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)
    
    def starting(self,chat_id,photo_id):
        if not (f'l{chat_id}' in self.db[photo_id].keys()):
            self.db[photo_id][f'l{chat_id}']={'likes':0,'dislikes':0}
        return None

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def add_lang(self,chat_id,lang):
        if not(chat_id in self.db['Users'].keys()):
            self.db['Users'][chat_id]['lang']=lang
    def get_lang(self,chat_id):
        return self.db['Users'][chat_id]['lang']
    def obuna(self,chat_id):
        return self.db['Users'][chat_id]['obuna']

