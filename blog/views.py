#-*- coding:UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from blog.models import Entries, Category, Comment, Chat
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import md5
import datetime

def index(request):
	category=Category.objects.all()
	writing=Entries.objects.all()[::-1]
	c=Comment.objects.all()
	message=0
	return render_to_response('index.html',{'message':message,'category':category,'writing':writing,'c':c})

def test(request):
	return render_to_response('test.html')

def blog(request, offset):
	offset=int(offset)
	e=Entries.objects.filter(id=offset)
	c=Comment.objects.filter(entry=Entries.objects.get(id=offset))
	return render_to_response('blog.html',{'offset':offset,'e':e,'c':c})

def blog_comment_delete(request, offset):
	offset=int(offset)
	try:
		d=Comment.objects.get(id=offset)
		a=d.entry.id
		e=Entries.objects.get(id=a)
		if e.cnumber>0:
			e.cnumber=e.cnumber-1
			e.save()
		d.delete()
	except:
		return HttpResponse('오류가 나고있습니다')
	return HttpResponseRedirect('/blog/'+str(a))

@csrf_exempt
def blog_comment(request, offset):
	offset=int(offset)
	e=Entries.objects.filter(id=offset)
	if not request.POST['name']:
		return HttpResponse(u'이름을 입력하세요')
	cmt_name=request.POST['name']
	cmt_content=request.POST['content']
	if not request.POST['content']:
		return HttpResponse(u'글 내용을 입력하세요')
	cmt_password=request.POST['password']
	if not request.POST['password']:
		return HttpResponse(u'비밀번호를 입력하세요')
	cmt_password = md5.md5(cmt_password).hexdigest()
	cmt=Comment()
	try:
		cmt.name=cmt_name
		cmt.password=cmt_password
		cmt.text=cmt_content
		ie=Entries.objects.get(id=request.POST['entry_id'])
		cmt.entry=ie
		ie.cnumber=ie.cnumber+1
		ie.save()
		cmt.save()
	except:
		return HttpResponse('오류가 나고 있습니다')
	c=Comment.objects.filter(entry=Entries.objects.get(id=offset))
	return render_to_response('blog.html',{'offset':offset,'e':e,'c':c})



@csrf_exempt
def ment_write(request):
	if request.POST['name'] and request.POST['ment']:
		m=Chat()
		m.name=request.POST['name']
		m.ment=request.POST['ment']
		try:
			m.save()
		except:
			return HttpResponse('멘트 입력 실패')
	return HttpResponse(m.name+':'+m.ment)

def fetch(request):
	m=Chat.objects.all()
	return HttpResponse(json.dumps({'m':m}), mimetype='application/json')


@csrf_exempt
def write(request):
	message=0
	if request.POST['title'] and request.POST['text']:
		w=Entries()
		w.title=request.POST['title']
		try:
			entry_category = Category.objects.get(id=request.POST['category'])
		except:
			return HttpResponse(u'이상한 글 갈래입니다')
		w.category=entry_category
		w.text=request.POST['text']
		try:
			w.save()
			message=1
		except:
			message=0
	category=Category.objects.all()
	writing=Entries.objects.all()[::-1]
	return render_to_response('index.html',{'message':message,'category':category,'writing':writing})

