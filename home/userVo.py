class User:
    def __init__(self, result):
        self.user_id = result[0]
        self.user_nodeid = result[1]
        self.user_name = result[2]
        self.user_birth = result[3]
        self.user_height = result[4]
        self.user_weight = result[5]
        self.user_sex = result[6]
        self.user_fhistory = result[7]
        self.user_smoking = result[8]
        self.user_drinking = result[9]
        self.user_pregnant = result[10]
        self.user_u_phone = result[11]
        self.user_bmi = result[12]
        self.user_from_date = result[13]
        self.user_to_date = result[14]
        self.user_token = result[15]
        self.user_nok = result[16]
        self.user_phone = result[17]

    ################# get method #########################3
    def get_user_id(self):
        return self.user_id
    
    def get_user_nodeid(self):
        return self.user_nodeid

    def get_user_name(self):
        return self.user_name

    def get_user_birth(self):
        return self.user_birth

    def get_user_height(self):
        return self.user_height

    def get_user_weight(self):
        return self.user_weight

    def get_user_sex(self):
        return self.user_sex

    def get_user_fhistory(self):
        return self.user_fhistory

    def get_user_smoking(self):
        return self.user_smoking

    def get_user_drinking(self):
        return self.user_drinking

    def get_user_pregnant(self):
        return self.user_pregnant

    def get_user_u_phone(self):
        return self.user_u_phone
    
    def get_user_bmi(self):
        return self.user_bmi

    def get_user_from_date(self):
        return self.user_from_date
    
    def get_user_to_date(self):
        return self.user_to_date
    
    def get_user_token(self):
        return self.user_token

    def get_user_nok(self):
        return self.user_nok

    def get_user_phone(self):
        return self.user_phone
    

    ################## set method #########################
    def set_user_id(self, id):
        self.user_id = id
    
    def set_user_nodeid(self, nodeid):
        self.user_nodeid = nodeid

    def set_user_name(self, name):
        self.user_name = name

    def set_user_birth(self, birth):
        self.user_birth = birth

    def set_user_height(self, height):
        self.user_height = height

    def set_user_weight(self, weight):
        self.user_weight = weight

    def set_user_sex(self, sex):
        self.user_sex = sex

    def set_user_fhistory(self, fhistory):
        self.user_fhistory = fhistory

    def set_user_smoking(self, smoking):
        self.user_smoking = smoking

    def set_user_drinking(self, drinking):
        self.user_drinking = drinking

    def set_user_pregnant(self, pregnant):
        self.user_pregnant = pregnant

    def set_user_u_phone(self, u_phone):
        self.user_u_phone = u_phone
    
    def set_user_bmi(self, bmi):
        self.user_bmi = bmi

    def set_user_from_date(self, from_date):
        self.user_from_date = from_date
    
    def set_user_to_date(self, to_date):
        self.user_to_date = to_date
    
    def set_user_token(self, token):
        self.user_token = token

    def set_user_nok(self, nok):
        self.user_nok = nok

    def set_user_phone(self, phone):
        self.user_phone = phone