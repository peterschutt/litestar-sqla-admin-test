from litestar import Litestar
from sqladmin import Admin, ModelView

from db import User, engine


admin = Admin(engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


admin.add_view(UserAdmin)

app = Litestar(plugins=[admin], debug=True)
