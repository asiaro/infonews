from flask import Flask
from info.models import app
from info import create_app



app=create_app("dev")
mgr=Manager(app)


mgr.add_command("mc",MigrateCommand)






if __name__=='__main__':
    mgr.run()


