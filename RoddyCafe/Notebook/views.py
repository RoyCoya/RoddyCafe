from Notebook.api import note as api_note, directory as api_directory, wangeditor as api_wangeditor
from Notebook.page import homepage as page_homepage, todo as page_todo, share as page_share, configurations as page_configurations
from Notebook.page import note as page_note, directory as page_directory

'''页面'''
# 四个主界面
def homepage(request): return page_homepage.homepage(request)
def todo(request): return page_todo.todo(request)
def share(request): return page_share.share(request)
def configurations(request): return page_configurations.configurations(request)

# 目录
def directory_specific(request, directory_id, is_from_todo): return page_directory.specific(request, directory_id, is_from_todo)
# 笔记
def note_new(request, directory_id): return page_note.new(request, directory_id)
def note_detail(request, note_id, is_from_homepage): return page_note.detail(request, note_id, is_from_homepage)
def note_edit(request, note_id, is_from_todo): return page_note.edit(request, note_id, is_from_todo)

'''接口'''
# 目录
def api_directory_new(request, directory_id): return api_directory.new(request, directory_id)
def api_directory_delete(request, directory_id): return api_directory.delete(request, directory_id)
def api_directory_move(request, dir_to_move_id, parent_id, child_id, is_first_child): return api_directory.move(request, dir_to_move_id, parent_id, child_id, is_first_child)
def api_directory_edit_name(request, directory_id): return api_directory.edit_name(request, directory_id)
def api_directory_edit_discription(request, directory_id): return api_directory.edit_discription(request, directory_id)

# 笔记
def api_note_delete(request, note_id): return api_note.delete(request, note_id)
def api_note_edit(request, note_id): return api_note.edit(request, note_id)
def api_note_move(request, note_id, directory_id): return api_note.move(request, note_id, directory_id)
def api_note_switch_pintop(request, note_id): return api_note.switch_pintop(request, note_id)
def api_note_switch_pending(request, note_id): return api_note.switch_pending(request, note_id)
def api_note_switch_shortcut(requst, note_id): return api_note.switch_shortcut(requst, note_id)

# wangeditor
def api_wangeditor_upload_img(request, note_id): return api_wangeditor.upload_img(request, note_id)
def api_wangeditor_upload_video(request, note_id): return api_wangeditor.upload_video(request, note_id)