
import import_file as f
values={
        "SNO":1
        }

def train_rex():
    values["main_kw"]=input("MAIN KEYWORD:")
    values["action_file"]=input("ACTION FILE:")
    f.db.insert_training_commands(values)
