from settings import TaggySettings
from repository.JSONRepository import JSONRepository
from ui.app import App
from logger import TaggyLogger
import model

logger = TaggyLogger()

repository = JSONRepository()

settings = TaggySettings()

#update_repository(SAMPLE_FOLDER)
#update_model_tree()
repository.load_tree(settings.sample_folder)
settings.load_settings()
print(model.Filesystem.tree)

app = App()
app.mainloop()

repository.save_tree(settings.sample_folder)
settings.save_settings()
#repository.close_connection()

