# mydiary/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Profile, Content, Comment, Tag
from .forms import ContentForm, CommentForm, ProfileForm, TagForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Content.objects.all()
    return render(request, 'home.html', {'posts_list':posts})

def new(request):
    if request.method == 'POST':
        form = ContentForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            user = request.user
            profile = Profile.objects.get(user=user)
            post.author = request.user.profile
            post.published_date = timezone.now()
            post.save()

            post.like_users.add(profile)
            profile.like_posts.add(post)
            post.like_count += 1
            post.save()
            
            return redirect('home')
    else:
        form = ContentForm()
    return render(request, 'new.html',{'form':form})

def detail(request, pk):
    post = get_object_or_404(Content, pk = pk)
    comment_list = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.published_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('detail', pk = pk)
    else :
        comment_form = CommentForm()
        tag_form = TagForm()
        user_name = request.user
    return render(request, 'detail.html', {'post':post, 'comment_list':comment_list, 'comment_form':comment_form, 'tag_form':tag_form, 'user':user_name})

def edit(request, index):
    post = get_object_or_404(Content, pk = index)
    if request.method=='POST':
        form = ContentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.published_date = timezone.now
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'edit.html',{'form':form})

def delete(request,pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect('home')

def delete_comment(request, pk, comment_pk) :
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect('detail',pk=pk)

def tag_add(request, pk):
    post = get_object_or_404(Content, pk=pk)
    tag_form = TagForm(request.POST)
    if tag_form.is_valid():
        tag = tag_form.save(commit=False)
        tag, created = Tag.objects.get_or_create(name=tag.name)
        post.tags.add(tag)
        return redirect('detail',pk=pk)

def tag_home(request):
    tags = Tag.objects.all()
    return render(request, 'tag.html', {'tags':tags})

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag_posts = tag.content_set.all()
    return render(request, 'tag_detail.html', {'tag':tag, 'tag_posts':tag_posts})

def tag_delete(request, pk, tag_pk):
    post = get_object_or_404(Content, pk=pk)
    tag = get_object_or_404(Tag, pk=tag_pk)
    post.tags.remove(tag)
    if tag.content_set.count() == 0 :
        tag.delete()
    return redirect('detail', pk=pk)

#검색기능
def search(request):
    posts = Content.objects.all().order_by('-pk')

    q = request.POST.get('q',"")

    if q:
        posts = posts.filter(title__icontains=q)
        return render(request, 'search.html', {'posts' : posts, 'q' : q})

    else:
        return render(request, 'search.html')


# 공구 참여 기능

@login_required
def post_like_toggle(request, post_id):
    post = get_object_or_404(Content, pk=post_id)
    profile = request.user.profile   
    check_like_post = profile.like_posts.filter(pk=post_id)

    if check_like_post.exists():
        post.like_users.remove(profile)
        profile.like_posts.remove(post)
        post.like_count -= 1
        post.save()
    elif post.like_count < post.limit:
        post.like_users.add(profile)
        profile.like_posts.add(post)
        post.like_count += 1
        post.save()

    return redirect('detail', post_id)

#profile생성기능
@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.add_message(request, messages.INFO, 'Welcome!! Now you can enjoy our community!')
            return redirect('home') 
    else:
        form = ProfileForm()
    
    return render(request, 'profile_create.html', {'form':form})
