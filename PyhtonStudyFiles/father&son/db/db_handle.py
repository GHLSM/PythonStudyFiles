import os
import pickle
from conf import settings


def save_data(obj):
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )
    # 文件夹创建
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    user_path = os.path.join(
        user_dir_path, obj.username
    )
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


def select_data(cls, username):
    # 由cls类获取类名
    user_dir_path = os.path.join(
        settings.DB_PATH, cls.__name__
    )
    user_path = os.path.join(
        user_dir_path, username
    )

    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj
