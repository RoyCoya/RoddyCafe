'''笔记操作'''

from django.shortcuts import redirect
from django.http import *
from django.conf import settings
from django.urls import reverse

from Notebook.models import *
from .common import *

# 新增笔记
def new(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dir = directory.objects.get(id=directory_id)
    user = request.user
    if user != dir.user: return HttpResponseForbidden('您无权在该目录中新增笔记')

    new_note = note(
        directory=dir,
        user=request.user,
        title=request.POST['note_title'],
        content=request.POST['note_content'],
    )
    new_note.save()

    return HttpResponse(new_note.id)

# 删除笔记
def delete(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    note_to_delete = note.objects.get(id=note_id)
    user = request.user
    if user != note_to_delete.user: return HttpResponseForbidden('您无权删除此笔记')

    note_to_delete.delete()
    
    dir = note_to_delete.directory
    return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(dir.id,)))

# 保存笔记编辑
def edit(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    noteEdited = note.objects.get(id=note_id)
    user = request.user
    if user != noteEdited.user: return HttpResponseForbidden('您无权编辑此笔记')

    noteEdited.content = request.POST['note_content_edited']
    noteEdited.save()
    
    return HttpResponse('编辑笔记成功')

# 笔记更换目录
def move(request,note_id,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    note_to_move = note.objects.get(id=note_id)
    user = request.user
    if user != note_to_move.user: return HttpResponseForbidden('您无权移动该目录。')
    
    target_directory = directory.objects.get(id=directory_id)
    note_to_move.directory = target_directory
    note_to_move.save()

    return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(directory_id,)))

# 笔记切换置顶状态
def switch_pintop(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    note_to_set_pin = note.objects.get(id=note_id)
    user = request.user
    if user != note_to_set_pin.user: return HttpResponseForbidden('您无权置顶此笔记')
    
    note_to_set_pin.isPinTop = request.POST['pintop_checked'].title()
    note_to_set_pin.save()

    return HttpResponse("笔记置顶成功")

# 笔记切换待编辑状态
def switch_pending(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    note_to_set_pending = note.objects.get(id=note_id)
    user = request.user
    if user != note_to_set_pending.user: return HttpResponseForbidden('您无权将此笔记设置为“未编辑”状态')

    note_to_set_pending.isPending = request.POST['pending_checked'].title()
    note_to_set_pending.save()

    return HttpResponse("笔记设置未编辑状态成功")