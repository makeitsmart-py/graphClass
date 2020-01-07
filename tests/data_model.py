from libs.ui_interface.data_model import DataModelEntity


class UserName(DataModelEntity):
    pass


class UserPassword(DataModelEntity):
    pass


class UserFriend(DataModelEntity):
    pass


class User(DataModelEntity):
    username = UserName()
    password = UserName()

