from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from items.models import item

from .models import conversation

from .forms import conversationmessageform

@login_required
def new_conversation(request, item_pk):
    items = get_object_or_404(item, pk = item_pk)

    if items.created_by == request.user :
        return redirect("Dashboard:index")
    
    conversations = conversation.objects.filter(items = items).filter(members__in = [request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)
    
    if request.method == "POST":
        form = conversationmessageform(request.POST)

        if form.is_valid():
            conversations = conversation.objects.create(items = items)
            conversations.members.add(request.user)
            conversations.members.add(items.created_by)
            conversations.save()

            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversations
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("items:Detail", pk = item_pk)
        
    else:
        form = conversationmessageform()

    return render(request, "conversation/new.html", {
            "form": form
        })

@login_required
def inbox(request):
    conversations = conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })


@login_required
def detail(request, pk):
    conversations = conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = conversationmessageform(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversations
            conversation_message.created_by = request.user
            conversation_message.save()

            conversations.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = conversationmessageform()

    return render(request, 'conversation/detail.html', {
        'conversations': conversations,
        'form': form
    })